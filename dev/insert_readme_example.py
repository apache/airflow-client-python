#!/usr/bin/env python3
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

if __name__ == '__main__':
    example = (BASE_DIR / "dev" / "test_python_client.py").read_text().splitlines()
    example = example[example.index("# under the License.")+1:]   # Remove license header
    readme_lines = (BASE_DIR / "README.md").read_text().splitlines()
    result_lines = []
    skip_lines = False
    changes_made = False
    for line in readme_lines:
        if line.strip().startswith("example python script:"):
            result_lines.append(line)
            result_lines.append("")
            result_lines.append("```python")
            result_lines.extend(example)
            result_lines.append("```")
            skip_lines = True
            changes_made = True
        else:
            if not skip_lines:
                result_lines.append(line)
            if line.strip() == "```":
                skip_lines = False
    (BASE_DIR / "README.md").write_text("\n".join(result_lines))
    if not changes_made:
        raise Exception("Could not find example python script in README.md to replace. "
                        "Please make sure `example python script:` line is in README.md")
