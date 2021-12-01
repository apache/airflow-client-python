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

You can find the prerequisites to release Apache Airflow Python Client in [README.md](README.md).

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


    # Example after cloning
    git clone https://github.com/apache/airflow-client-python.git airflow-client
    cd airflow-client
    export CLIENT_REPO_ROOT=$(pwd)
    ```

- Set your version to 2.0.0 in `setup.py` (without the RC tag)
- Commit the version change.

- Tag your release

    ```shell script
    git tag -s ${VERSION}
    ```

- Clean the checkout: the sdist step below will

    ```shell script
    git clean -fxd
    ```

- Tarball the repo

    ```shell script
    git archive --format=tar.gz ${VERSION} --prefix=apache-airflow-client-${VERSION_WITHOUT_RC}/ -o apache-airflow-client-${VERSION_WITHOUT_RC}-source.tar.gz
    ```

- Generate sdist

  NOTE: Make sure your checkout is clean at this stage - any untracked or changed files will otherwise be included
  in the file produced.

    ```shell script
    python setup.py sdist bdist_wheel
    ```

- Rename the sdist

    ```shell script
    mv dist/apache-airflow-client-${VERSION_WITHOUT_RC}.tar.gz apache-airflow-client-${VERSION_WITHOUT_RC}-bin.tar.gz
    mv dist/apache_airflow_client-${VERSION_WITHOUT_RC}-py3-none-any.whl apache_airflow_client-${VERSION_WITHOUT_RC}-py3-none-any.whl
    ```

- Generate SHA512/ASC (If you have not generated a key yet, generate it by following instructions on
  http://www.apache.org/dev/openpgp.html#key-gen-generate-key)

    ```shell script
    ${CLIENT_REPO_ROOT}/dev/sign.sh apache-airflow-client-${VERSION_WITHOUT_RC}-source.tar.gz
    ${CLIENT_REPO_ROOT}/dev/sign.sh apache-airflow-client-${VERSION_WITHOUT_RC}-bin.tar.gz
    ${CLIENT_REPO_ROOT}/dev/sign.sh apache_airflow_client-${VERSION_WITHOUT_RC}-py3-none-any.whl
    ```

- Push the artifacts to ASF dev dist repo

```
# First clone the repo
svn checkout https://dist.apache.org/repos/dist/dev/airflow airflow-dev

# Create new folder for the release
cd airflow-dev/clients/python
svn mkdir ${VERSION}

# Move the artifacts to svn folder & commit
mv ${CLIENT_REPO_ROOT}/apache{-,_}*client-${VERSION_WITHOUT_RC}* ${VERSION}/
cd ${VERSION}
svn add *
svn commit -m "Add artifacts for Apache Airflow Python Client ${VERSION}"
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
  `twine upload -r pypi dist/*`

- Again, confirm that the package is available here:
  https://pypi.python.org/pypi/apache-airflow-client

It is important to stress that this snapshot should not be named "release", and it
is not supposed to be used by and advertised to the end-users who do not read the devlist.

- Push Tag for the release candidate

    ```shell script
    git push origin ${VERSION}
    ```

## Prepare Vote email on the Airflow Client release candidate
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#prepare-vote-email-on-the-apache-airflow-release-candidate) (just replace Airflow with Airflow Client).

# Verify the release candidate by PMCs
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#verify-the-release-candidate-by-pmcs).

## SVN check
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#svn-check) (just replace Airflow with Airflow Client).

## Licence check
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#licence-check).

## Signature check
See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#signature-check).



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

See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#publish-the-final-apache-airflow-release) (just replace Airflow with Airflow Client).

## Publish release to SVN

```shell script
# First clone the repo
export RC=2.0.0rc1
export VERSION=${RC/rc?/}
svn checkout https://dist.apache.org/repos/dist/release/airflow airflow-release

# Create new folder for the release
cd airflow-release/clients/python
svn mkdir ${VERSION}
cd ${VERSION}

# Move the artifacts to svn folder & commit
for f in ../../../../airflow-dev/clients/python/$RC/*; do svn cp $f . ; done
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

- Clean & Build the package:

    ```shell script
    git clean -fxd
    python setup.py sdist bdist_wheel
    ```

- Verify the artifacts that would be uploaded:

    ```shell script
    twine check dist/*
    ```

- Upload the package to PyPi's test environment:

    ```shell script
    twine upload --repository-url=https://test.pypi.org/legacy/ dist/*
    ```

- Verify that the test package looks good by downloading it and installing it into a virtual environment.
  The package download link is available at: https://test.pypi.org/project/apache-airflow-client/#files

- Upload the package to PyPi's production environment:

    ```shell script
    twine upload -r pypi dist/*
    ```

- Again, confirm that the package is available here: https://pypi.python.org/pypi/apache-airflow-client

## Update CHANGELOG.md

- Get a diff between the last version and the current version:

    ```shell script
    git log 1.0.0..2.0.0 --pretty=oneline
    ```

- Update CHANGELOG.md with the details, and commit it.

- Push Tag for the final version

    ```shell script
    git tag ${VERSION}
    git push origin ${VERSION}
    ```

## Notify developers of release

See Airflow process documented [here](https://github.com/apache/airflow/blob/master/dev/README_RELEASE_AIRFLOW.md#notify-developers-of-release) (just replace Airflow with Airflow Client)
