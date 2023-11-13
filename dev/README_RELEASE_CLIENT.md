<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
 -->

# Release Process

Typically, releases are done coinciding with major and minor releases to Airflow. Therefore, a release of (for example) 
2.3.0 of this client would correspond with 2.3.X of Airflow.

The Python client is generated using Airflow's [openapi spec](https://github.com/apache/airflow/blob/master/clients/gen/python.sh).
To update the client for new APIs do the following steps:

```bash
# set the version of the client
export VERSION=2.0.0rc1
# clone this repo
git clone git@github.com:apache/airflow-client-python.git
cd airflow-client-python
export CLIENT_REPO_ROOT=$(pwd)
cd ..

# clone Airflow repo (if not already)
git clone git@github.com:apache/airflow.git
cd airflow
export AIRFLOW_REPO_ROOT=$(pwd)
```
Edit the file `airflow/airflow/api_connexion/openapi/v1.yaml`
Make sure it has the following `securitySchema`s listed under security `section`
```yaml
security:
  - Basic: []
  - GoogleOpenId: []
  - Kerberos: []
```
If your deployment of Airflow uses any different authentication mechanism than the three listed above, you might need to make further changes to the `v1.yaml` and generate your own client, see [OpenAPI Schema specification](https://swagger.io/docs/specification/authentication/) for details.
(*These changes should not be commited to the upstream `v1.yaml` [as it will generate misleading openapi documentaion](https://github.com/apache/airflow/pull/17174)*)


```bash

# bump up the version in python.sh & run the following command
${AIRFLOW_REPO_ROOT}/clients/gen/python.sh airflow/api_connexion/openapi/v1.yaml ${CLIENT_REPO_ROOT}/airflow_client

cd ${CLIENT_REPO_ROOT}
```

- Set your version in `setup.py` (without the RC tag)

- Get a diff between the last airflow version and the current airflow version
  which this release is based on:

      ```shell script
      # Run this command in Airflow Repo
      git log 2.3.0..2.5.0 --pretty=oneline -- airflow/api_connexion/openapi/v1.yaml
      ```

- Update CHANGELOG.md with the details.
- Commit the Changes with the message "Add Client Version ${VERSION}":
  ```shell script
  git add .
  git commit -m "Add Client Version ${VERSION}"
  ```
- Raise a PR in airflow-client-python with the above changes
- Merge the above PR when approved before proceeding

# Prepare the Apache Airflow Python Client Package RC

## Build RC artifacts

The Release Candidate artifacts we vote upon should be the exact ones we vote against, without any modification than
renaming – i.e. the contents of the files must be the same between voted release candidate and final release. Because
of this the version in the built artifacts that will become the official Apache releases must not include the rcN suffix.

- Set environment variables
  
    ```shell script
    # Set Version
    export VERSION=2.0.0rc1
    export VERSION_WITHOUT_RC=${VERSION%rc?}
    # Set the airflow version that this release is based
    export AIRFLOW_VERSION=2.1.4 


    # Example after cloning
    git clone https://github.com/apache/airflow-client-python.git 
    cd airflow-client-python
    export CLIENT_REPO_ROOT=$(pwd)
    ```

- Tag your release

    ```shell script
    git tag -s ${VERSION} -m "Airflow Python Client {VERSION}"
    ```

- Clean the checkout: the sdist step below will

    ```shell script
    git clean -fxd
    ```

- Tarball the repo

    ```shell script
    mkdir dist
    git archive --format=tar.gz ${VERSION} --prefix=apache-airflow-client-${VERSION_WITHOUT_RC}/ -o dist/apache-airflow-client-${VERSION_WITHOUT_RC}-source.tar.gz
    ```

- Generate sdist

  NOTE: Make sure your checkout is clean at this stage - any untracked or changed files will otherwise be included
  in the file produced.

    ```shell script
    pip install wheel
    python setup.py sdist bdist_wheel
    ```

- Rename the sdist

    ```shell script
    mv dist/apache-airflow-client-${VERSION_WITHOUT_RC}.tar.gz dist/apache-airflow-client-${VERSION_WITHOUT_RC}-bin.tar.gz
    mv dist/apache_airflow_client-${VERSION_WITHOUT_RC}-py3-none-any.whl dist/apache_airflow_client-${VERSION_WITHOUT_RC}-py3-none-any.whl
    ```

- Generate SHA512/ASC (If you have not generated a key yet, generate it by following instructions on
  http://www.apache.org/dev/openpgp.html#key-gen-generate-key)

    ```shell script
    pushd dist
    ${CLIENT_REPO_ROOT}/dev/sign.sh *
    popd
    ```

- Push the artifacts to ASF dev dist repo

```shell script
# First clone the repo
svn checkout https://dist.apache.org/repos/dist/dev/airflow airflow-dev

# Create new folder for the release
cd airflow-dev/clients/python
svn mkdir ${VERSION}

# Move the artifacts to svn folder & commit
mv ${CLIENT_REPO_ROOT}/dist/apache{-,_}*client-${VERSION_WITHOUT_RC}* ${VERSION}/
cd ${VERSION}
svn add *
svn commit -m "Add artifacts for Apache Airflow Python Client ${VERSION}"
cd ${CLIENT_REPO_ROOT}
rm -rf airflow-dev
```

## Prepare PyPI convenience "snapshot" packages

At this point we have the artefact that we vote on, but as a convenience to developers we also want to
publish "snapshots" of the RC builds to pypi for installing via pip.

To do this we need to

- Build the package:

    ```shell script
    cd ${CLIENT_REPO_ROOT}
    python setup.py egg_info --tag-build "$(sed -e "s/^[0-9.]*//" <<<"$VERSION")" sdist bdist_wheel
    ```

- Verify the artifacts that would be uploaded:

    ```shell script
    twine check dist/*
    ```

- Upload the package to PyPi's test environment:

    ```shell script
    twine upload --repository-url=https://test.pypi.org/legacy/ dist/*
    ```

- Verify that the test package looks good by downloading it and installing it into a virtual environment. The package
  download link is available at:
  https://test.pypi.org/project/apache-airflow-client/#files

  Or via pypi
  pip install -i https://test.pypi.org/simple/ apache-airflow-client==${VERSION}

- Upload the package to PyPi's production environment:

  ```shell script
  twine upload -r pypi dist/*
  ```

- Again, confirm that the package is available here:
  https://pypi.python.org/pypi/apache-airflow-client

It is important to stress that this snapshot should not be named "release", and it
is not supposed to be used by and advertised to the end-users who do not read the devlist.

- Push Tag for the release candidate

```shell script
git push origin ${VERSION}
```

## Prepare Vote email on the Airflow Client release candidate

Subject:

```shell script
cat <<EOF
[VOTE] Release Airflow Python Client ${VERSION_WITHOUT_RC} from ${VERSION}
EOF
```

Body:
  
```shell script
cat <<EOF
Hey fellow Airflowers,

I have cut the release candidate for the Airflow Python Client ${VERSION}.
The client consists of APIs corresponding to REST APIs available in
*Apache Airflow ${AIRFLOW_VERSION}*. This email is calling for a vote on
the release, which will last for 72 hours. Consider this my (binding) +1.

Airflow Client ${VERSION} is available at:
https://dist.apache.org/repos/dist/dev/airflow/clients/python/$VERSION/

Or also available at PyPI:
https://pypi.org/project/apache-airflow-client/$VERSION/

*apache-airflow-client-${VERSION}-source.tar.gz* is a source release that comes with
INSTALL instructions.
*apache-airflow-client-${VERSION}-bin.tar.gz* is the binary Python "sdist" release.

Public keys are available at:
https://dist.apache.org/repos/dist/release/airflow/KEYS

Only votes from PMC members are binding, but the release manager should
encourage members of the community to test the release and vote with
"(non-binding)".

*Changelog:*

*Major changes:*
...

*Major fixes:*
...

*New API supported:*
...

Cheers,
<your name>
EOF
```

# Verify the release candidate by PMCs
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#verify-the-release-candidate-by-pmcs).

## SVN check
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#svn-check) (just replace Airflow with Airflow Client).

## Licence check
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#licence-check).

## Signature check
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#signature-check).

## Sources check

The code of the Python Client is generated using OpenAPI generator and the generated code is committed to
the repository, therefore the Source code check should consist of two steps:

1. Checkout the release tag of the "airflow-client-python"
2. Follow the [Release process](#release-process) above and generate client's code above
3. Run ``git diff`` to see the differences - review them. Generally the code generated should only contain
   small differences regarding authentication.
4. git reset --hard <RELEASE_TAG>

Compare the sources with the packaged sources following the process described in Airflow:
[here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#signature-check).

# Verify release candidates by Contributors
This can be done (and we encourage to) by any of the Contributors. In fact, it's best if the
actual users of Airflow Client test it in their own staging/test installations. Each release candidate
is available on PyPI apart from SVN packages, so everyone should be able to install
the release candidate version of Airflow Client via simply (<VERSION> is 2.0.0 for example, and <X> is
release candidate number 1,2,3,....).

```shell script
pip install apache-airflow-client==<VERSION>rc<X>
```

Once you install and run Airflow Client, you should perform any verification you see as necessary to check
that the client works as you expected.

# Publish the final Apache Airflow client release

## Summarize the voting for the Apache Airflow client release

```shell script
Hello,

Apache Airflow Python Client 2.5.0 (based on RC1) has been accepted.

3 "+1" binding votes received:
- Ephraim Anierobi
- Jarek Potiuk
- Jed Cunningham


1 "+1" non-binding votes received:

- Pierre Jeambrun

Vote thread:
https://lists.apache.org/thread/1qcj0r67dff3zg0w2vyfhr30fx9xtp3y

I'll continue with the release process, and the release announcement will follow shortly.

Cheers,
<your name>
```

## Publish release to SVN

```shell script
# Go to Airflow python client sources first
cd <YOUR_AIRFLOW_CLIENT_REPO_ROOT>
export CLIENT_REPO_ROOT="$(pwd)"
cd ..
# Clone the AS
[ -d asf-dist ] || svn checkout --depth=immediates https://dist.apache.org/repos/dist asf-dist
svn update --set-depth=infinity asf-dist/{release,dev}/airflow
CLIENT_DEV_SVN="${PWD}/asf-dist/dev/airflow/clients/python"
CLIENT_RELEASE_SVN="${PWD}/asf-dist/release/airflow/clients/python"
cd "${CLIENT_RELEASE_SVN}"

export RC=2.0.0rc1
export VERSION=${RC/rc?/}

# Create new folder for the release
svn mkdir ${VERSION}
cd ${VERSION}

# Move the artifacts to svn folder & commit
for f in ${CLIENT_DEV_SVN}/$RC/*; do 
  svn cp $f . ; 
done
svn commit -m "Release Apache Airflow Python Client ${VERSION} from ${RC}"

# Remove old release
# http://www.apache.org/legal/release-policy.html#when-to-archive
cd ..
export PREVIOUS_VERSION=1.0.0
svn rm ${PREVIOUS_VERSION}
svn commit -m "Remove old release: ${PREVIOUS_VERSION}"
```

Verify that the packages appear in [airflow](https://dist.apache.org/repos/dist/release/airflow/clients/python)

## Prepare PyPI "release" packages

At this point we release an official package:

- Copy the packages from the SVN into the dist folder in CLIENT_REPO_ROOT:

    ```shell script
    rm -rf ${CLIENT_REPO_ROOT}/dist
    mkdir ${CLIENT_REPO_ROOT}/dist
    cp ${CLIENT_RELEASE_SVN}/${VERSION}/apache-airflow-client-${VERSION}-bin.tar.gz ${CLIENT_REPO_ROOT}/dist/
    cp ${CLIENT_RELEASE_SVN}/${VERSION}/apache_airflow_client-${VERSION}-py3-none-any.whl ${CLIENT_REPO_ROOT}/dist/
    # Remove the -bin
    mv ${CLIENT_REPO_ROOT}/dist/apache-airflow-client-${VERSION}-bin.tar.gz ${CLIENT_REPO_ROOT}/dist/apache-airflow-client-${VERSION}.tar.gz
    ```

- Verify the artifacts that would be uploaded:

    ```shell script
    twine check dist/*
    ```

- Upload the package to PyPi's production environment:

    ```shell script
    twine upload -r pypi dist/*
    ```

- Confirm that the package is available here: https://pypi.python.org/pypi/apache-airflow-client

- Push Tag for the final version

    ```shell script
    git tag ${VERSION}
    git push origin ${VERSION}
    ```

## Create release on GitHub

Create a new release on GitHub with the release notes and assets from the release svn.

## Notify developers of release

Notify users@airflow.apache.org (cc'ing dev@airflow.apache.org) that the artifacts have been published:

Subject:

```shell script
    cat <<EOF
    [ANNOUNCE] Apache Airflow Python Client ${VERSION} Released
    EOF
```
Body: 

```shell script
    cat <<EOF
    Dear Airflow community,

I'm happy to announce that Airflow Python Client ${VERSION} was just released.

We also made this version available on PyPI for convenience:
`pip install apache-airflow-client`
https://pypi.org/project/apache-airflow-client/${VERSION}/

The documentation is available at:
https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html

Find the changelog here for more details:
https://github.com/apache/airflow-client-python/blob/main/CHANGELOG.md


Cheers,
<your name>
EOF
```
Send the same email to announce@apache.org, except change the opening line to Dear community,. It is more reliable to send it via the web ui at https://lists.apache.org/list.html?announce@apache.org (press "c" to compose a new thread)



## Add release data to Apache Committee Report Helper

Add the release data (version and date) at: https://reporter.apache.org/addrelease.html?airflow
