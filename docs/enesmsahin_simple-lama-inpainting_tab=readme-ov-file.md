├── .flake8
├── .github
    └── workflows
    │   └── python-package.yml
├── .gitignore
├── LICENSE
├── README.md
├── poetry.lock
├── pyproject.toml
├── simple_lama_inpainting
    ├── __init__.py
    ├── cli.py
    ├── models
    │   ├── __init__.py
    │   └── model.py
    └── utils
    │   ├── __init__.py
    │   └── util.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── data
        ├── image_1.png
        ├── mask_1.png
        └── out_1.png
    └── test_lama.py


/.flake8:
-----------------------

[flake8]
max-line-length = 88
extend-ignore = E203

-----------------------

/.github/workflows/python-package.yml:
-----------------------

# This workflow will install Python dependencies, run tests and lint with a variety of Python versions
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python package

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    #----------------------------------------------
    #  -----  install & configure poetry  -----
    #----------------------------------------------
    - name: Install Poetry Action
      uses: snok/install-poetry@v1.3.3
      with:
        virtualenvs-create: true
        virtualenvs-in-project: true
        installer-parallel: true
    
    #----------------------------------------------
    #       load cached venv if cache exists
    #----------------------------------------------
    - name: Load cached venv
      id: cached-poetry-dependencies
      uses: actions/cache@v3
      with:
        path: .venv
        key: venv-${{ runner.os }}-${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('**/poetry.lock') }}

    #----------------------------------------------
    # install dependencies if cache does not exist
    #----------------------------------------------
    - name: Install dependencies
      if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
      run: poetry install --no-interaction --no-root

    #----------------------------------------------
    # install your root project, if required
    #----------------------------------------------
    - name: Install project
      run: poetry install --no-interaction

    # - name: Lint with flake8
    #  run: |
    #    # stop the build if there are Python syntax errors or undefined names
    #    poetry run flake8 -v .
    - name: Test with pytest
      run: |
        poetry run pytest


-----------------------

/.gitignore:
-----------------------

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

.DS_Store

-----------------------

/LICENSE:
-----------------------

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


-----------------------

/README.md:
-----------------------

# simple-lama-inpainting

<div align="center">
Simple pip package for LaMa[1] inpainting.<br>
<a href="https://badge.fury.io/py/simple-lama-inpainting"><img src="https://badge.fury.io/py/simple-lama-inpainting.svg" alt="PyPI version" height="18"></a>
</div>

## Installation
```
pip install simple-lama-inpainting
```

## Usage
### CLI
```
simple_lama <path_to_input_image> <path_to_mask_image> <path_to_output_image>
```

### Integration to Your Code
Input formats: `np.ndarray` or `PIL.Image.Image`. (3 channel input image & 1 channel binary mask image where pixels with 255 will be inpainted). \
Output format: `PIL.Image.Image`
```python
from simple_lama_inpainting import SimpleLama
from PIL import Image

simple_lama = SimpleLama()

img_path = "image.png"
mask_path = "mask.png"

image = Image.open(img_path)
mask = Image.open(mask_path).convert('L')

result = simple_lama(image, mask)
result.save("inpainted.png")
```

## Sources
[1] Suvorov, R., Logacheva, E., Mashikhin, A., Remizova, A., Ashukha, A., Silvestrov, A., Kong, N., Goka, H., Park, K., & Lempitsky, V. (2021). Resolution-robust Large Mask Inpainting with Fourier Convolutions. arXiv preprint arXiv:2109.07161. \
[2] https://github.com/saic-mdal/lama \
[3] https://github.com/Sanster/lama-cleaner


-----------------------

/poetry.lock:
-----------------------

# This file is automatically @generated by Poetry 1.5.1 and should not be changed by hand.

[[package]]
name = "black"
version = "23.7.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.8"
files = [
    {file = "black-23.7.0-cp310-cp310-macosx_10_16_arm64.whl", hash = "sha256:5c4bc552ab52f6c1c506ccae05681fab58c3f72d59ae6e6639e8885e94fe2587"},
    {file = "black-23.7.0-cp310-cp310-macosx_10_16_universal2.whl", hash = "sha256:552513d5cd5694590d7ef6f46e1767a4df9af168d449ff767b13b084c020e63f"},
    {file = "black-23.7.0-cp310-cp310-macosx_10_16_x86_64.whl", hash = "sha256:86cee259349b4448adb4ef9b204bb4467aae74a386bce85d56ba4f5dc0da27be"},
    {file = "black-23.7.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:501387a9edcb75d7ae8a4412bb8749900386eaef258f1aefab18adddea1936bc"},
    {file = "black-23.7.0-cp310-cp310-win_amd64.whl", hash = "sha256:fb074d8b213749fa1d077d630db0d5f8cc3b2ae63587ad4116e8a436e9bbe995"},
    {file = "black-23.7.0-cp311-cp311-macosx_10_16_arm64.whl", hash = "sha256:b5b0ee6d96b345a8b420100b7d71ebfdd19fab5e8301aff48ec270042cd40ac2"},
    {file = "black-23.7.0-cp311-cp311-macosx_10_16_universal2.whl", hash = "sha256:893695a76b140881531062d48476ebe4a48f5d1e9388177e175d76234ca247cd"},
    {file = "black-23.7.0-cp311-cp311-macosx_10_16_x86_64.whl", hash = "sha256:c333286dc3ddca6fdff74670b911cccedacb4ef0a60b34e491b8a67c833b343a"},
    {file = "black-23.7.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:831d8f54c3a8c8cf55f64d0422ee875eecac26f5f649fb6c1df65316b67c8926"},
    {file = "black-23.7.0-cp311-cp311-win_amd64.whl", hash = "sha256:7f3bf2dec7d541b4619b8ce526bda74a6b0bffc480a163fed32eb8b3c9aed8ad"},
    {file = "black-23.7.0-cp38-cp38-macosx_10_16_arm64.whl", hash = "sha256:f9062af71c59c004cd519e2fb8f5d25d39e46d3af011b41ab43b9c74e27e236f"},
    {file = "black-23.7.0-cp38-cp38-macosx_10_16_universal2.whl", hash = "sha256:01ede61aac8c154b55f35301fac3e730baf0c9cf8120f65a9cd61a81cfb4a0c3"},
    {file = "black-23.7.0-cp38-cp38-macosx_10_16_x86_64.whl", hash = "sha256:327a8c2550ddc573b51e2c352adb88143464bb9d92c10416feb86b0f5aee5ff6"},
    {file = "black-23.7.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6d1c6022b86f83b632d06f2b02774134def5d4d4f1dac8bef16d90cda18ba28a"},
    {file = "black-23.7.0-cp38-cp38-win_amd64.whl", hash = "sha256:27eb7a0c71604d5de083757fbdb245b1a4fae60e9596514c6ec497eb63f95320"},
    {file = "black-23.7.0-cp39-cp39-macosx_10_16_arm64.whl", hash = "sha256:8417dbd2f57b5701492cd46edcecc4f9208dc75529bcf76c514864e48da867d9"},
    {file = "black-23.7.0-cp39-cp39-macosx_10_16_universal2.whl", hash = "sha256:47e56d83aad53ca140da0af87678fb38e44fd6bc0af71eebab2d1f59b1acf1d3"},
    {file = "black-23.7.0-cp39-cp39-macosx_10_16_x86_64.whl", hash = "sha256:25cc308838fe71f7065df53aedd20327969d05671bac95b38fdf37ebe70ac087"},
    {file = "black-23.7.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:642496b675095d423f9b8448243336f8ec71c9d4d57ec17bf795b67f08132a91"},
    {file = "black-23.7.0-cp39-cp39-win_amd64.whl", hash = "sha256:ad0014efc7acf0bd745792bd0d8857413652979200ab924fbf239062adc12491"},
    {file = "black-23.7.0-py3-none-any.whl", hash = "sha256:9fd59d418c60c0348505f2ddf9609c1e1de8e7493eab96198fc89d9f865e7a96"},
    {file = "black-23.7.0.tar.gz", hash = "sha256:022a582720b0d9480ed82576c920a8c1dde97cc38ff11d8d8859b3bd6ca9eedb"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.7.4)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "certifi"
version = "2023.7.22"
description = "Python package for providing Mozilla's CA Bundle."
optional = false
python-versions = ">=3.6"
files = [
    {file = "certifi-2023.7.22-py3-none-any.whl", hash = "sha256:92d6037539857d8206b8f6ae472e8b77db8058fec5937a1ef3f54304089edbb9"},
    {file = "certifi-2023.7.22.tar.gz", hash = "sha256:539cc1d13202e33ca466e88b2807e29f4c13049d6d87031a3c110744495cb082"},
]

[[package]]
name = "charset-normalizer"
version = "3.2.0"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
optional = false
python-versions = ">=3.7.0"
files = [
    {file = "charset-normalizer-3.2.0.tar.gz", hash = "sha256:3bb3d25a8e6c0aedd251753a79ae98a093c7e7b471faa3aa9a93a81431987ace"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:0b87549028f680ca955556e3bd57013ab47474c3124dc069faa0b6545b6c9710"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:7c70087bfee18a42b4040bb9ec1ca15a08242cf5867c58726530bdf3945672ed"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:a103b3a7069b62f5d4890ae1b8f0597618f628b286b03d4bc9195230b154bfa9"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:94aea8eff76ee6d1cdacb07dd2123a68283cb5569e0250feab1240058f53b623"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:db901e2ac34c931d73054d9797383d0f8009991e723dab15109740a63e7f902a"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b0dac0ff919ba34d4df1b6131f59ce95b08b9065233446be7e459f95554c0dc8"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:193cbc708ea3aca45e7221ae58f0fd63f933753a9bfb498a3b474878f12caaad"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:09393e1b2a9461950b1c9a45d5fd251dc7c6f228acab64da1c9c0165d9c7765c"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:baacc6aee0b2ef6f3d308e197b5d7a81c0e70b06beae1f1fcacffdbd124fe0e3"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:bf420121d4c8dce6b889f0e8e4ec0ca34b7f40186203f06a946fa0276ba54029"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-musllinux_1_1_ppc64le.whl", hash = "sha256:c04a46716adde8d927adb9457bbe39cf473e1e2c2f5d0a16ceb837e5d841ad4f"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-musllinux_1_1_s390x.whl", hash = "sha256:aaf63899c94de41fe3cf934601b0f7ccb6b428c6e4eeb80da72c58eab077b19a"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:d62e51710986674142526ab9f78663ca2b0726066ae26b78b22e0f5e571238dd"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-win32.whl", hash = "sha256:04e57ab9fbf9607b77f7d057974694b4f6b142da9ed4a199859d9d4d5c63fe96"},
    {file = "charset_normalizer-3.2.0-cp310-cp310-win_amd64.whl", hash = "sha256:48021783bdf96e3d6de03a6e39a1171ed5bd7e8bb93fc84cc649d11490f87cea"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:4957669ef390f0e6719db3613ab3a7631e68424604a7b448f079bee145da6e09"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:46fb8c61d794b78ec7134a715a3e564aafc8f6b5e338417cb19fe9f57a5a9bf2"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:f779d3ad205f108d14e99bb3859aa7dd8e9c68874617c72354d7ecaec2a054ac"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f25c229a6ba38a35ae6e25ca1264621cc25d4d38dca2942a7fce0b67a4efe918"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2efb1bd13885392adfda4614c33d3b68dee4921fd0ac1d3988f8cbb7d589e72a"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:1f30b48dd7fa1474554b0b0f3fdfdd4c13b5c737a3c6284d3cdc424ec0ffff3a"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:246de67b99b6851627d945db38147d1b209a899311b1305dd84916f2b88526c6"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:9bd9b3b31adcb054116447ea22caa61a285d92e94d710aa5ec97992ff5eb7cf3"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:8c2f5e83493748286002f9369f3e6607c565a6a90425a3a1fef5ae32a36d749d"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:3170c9399da12c9dc66366e9d14da8bf7147e1e9d9ea566067bbce7bb74bd9c2"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-musllinux_1_1_ppc64le.whl", hash = "sha256:7a4826ad2bd6b07ca615c74ab91f32f6c96d08f6fcc3902ceeedaec8cdc3bcd6"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-musllinux_1_1_s390x.whl", hash = "sha256:3b1613dd5aee995ec6d4c69f00378bbd07614702a315a2cf6c1d21461fe17c23"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:9e608aafdb55eb9f255034709e20d5a83b6d60c054df0802fa9c9883d0a937aa"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-win32.whl", hash = "sha256:f2a1d0fd4242bd8643ce6f98927cf9c04540af6efa92323e9d3124f57727bfc1"},
    {file = "charset_normalizer-3.2.0-cp311-cp311-win_amd64.whl", hash = "sha256:681eb3d7e02e3c3655d1b16059fbfb605ac464c834a0c629048a30fad2b27489"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:c57921cda3a80d0f2b8aec7e25c8aa14479ea92b5b51b6876d975d925a2ea346"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:41b25eaa7d15909cf3ac4c96088c1f266a9a93ec44f87f1d13d4a0e86c81b982"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f058f6963fd82eb143c692cecdc89e075fa0828db2e5b291070485390b2f1c9c"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a7647ebdfb9682b7bb97e2a5e7cb6ae735b1c25008a70b906aecca294ee96cf4"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eef9df1eefada2c09a5e7a40991b9fc6ac6ef20b1372abd48d2794a316dc0449"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e03b8895a6990c9ab2cdcd0f2fe44088ca1c65ae592b8f795c3294af00a461c3"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:ee4006268ed33370957f55bf2e6f4d263eaf4dc3cfc473d1d90baff6ed36ce4a"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:c4983bf937209c57240cff65906b18bb35e64ae872da6a0db937d7b4af845dd7"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-musllinux_1_1_ppc64le.whl", hash = "sha256:3bb7fda7260735efe66d5107fb7e6af6a7c04c7fce9b2514e04b7a74b06bf5dd"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-musllinux_1_1_s390x.whl", hash = "sha256:72814c01533f51d68702802d74f77ea026b5ec52793c791e2da806a3844a46c3"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:70c610f6cbe4b9fce272c407dd9d07e33e6bf7b4aa1b7ffb6f6ded8e634e3592"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-win32.whl", hash = "sha256:a401b4598e5d3f4a9a811f3daf42ee2291790c7f9d74b18d75d6e21dda98a1a1"},
    {file = "charset_normalizer-3.2.0-cp37-cp37m-win_amd64.whl", hash = "sha256:c0b21078a4b56965e2b12f247467b234734491897e99c1d51cee628da9786959"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:95eb302ff792e12aba9a8b8f8474ab229a83c103d74a750ec0bd1c1eea32e669"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:1a100c6d595a7f316f1b6f01d20815d916e75ff98c27a01ae817439ea7726329"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:6339d047dab2780cc6220f46306628e04d9750f02f983ddb37439ca47ced7149"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e4b749b9cc6ee664a3300bb3a273c1ca8068c46be705b6c31cf5d276f8628a94"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a38856a971c602f98472050165cea2cdc97709240373041b69030be15047691f"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f87f746ee241d30d6ed93969de31e5ffd09a2961a051e60ae6bddde9ec3583aa"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:89f1b185a01fe560bc8ae5f619e924407efca2191b56ce749ec84982fc59a32a"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e1c8a2f4c69e08e89632defbfabec2feb8a8d99edc9f89ce33c4b9e36ab63037"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:2f4ac36d8e2b4cc1aa71df3dd84ff8efbe3bfb97ac41242fbcfc053c67434f46"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:a386ebe437176aab38c041de1260cd3ea459c6ce5263594399880bbc398225b2"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-musllinux_1_1_ppc64le.whl", hash = "sha256:ccd16eb18a849fd8dcb23e23380e2f0a354e8daa0c984b8a732d9cfaba3a776d"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-musllinux_1_1_s390x.whl", hash = "sha256:e6a5bf2cba5ae1bb80b154ed68a3cfa2fa00fde979a7f50d6598d3e17d9ac20c"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:45de3f87179c1823e6d9e32156fb14c1927fcc9aba21433f088fdfb555b77c10"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-win32.whl", hash = "sha256:1000fba1057b92a65daec275aec30586c3de2401ccdcd41f8a5c1e2c87078706"},
    {file = "charset_normalizer-3.2.0-cp38-cp38-win_amd64.whl", hash = "sha256:8b2c760cfc7042b27ebdb4a43a4453bd829a5742503599144d54a032c5dc7e9e"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:855eafa5d5a2034b4621c74925d89c5efef61418570e5ef9b37717d9c796419c"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:203f0c8871d5a7987be20c72442488a0b8cfd0f43b7973771640fc593f56321f"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:e857a2232ba53ae940d3456f7533ce6ca98b81917d47adc3c7fd55dad8fab858"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5e86d77b090dbddbe78867a0275cb4df08ea195e660f1f7f13435a4649e954e5"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c4fb39a81950ec280984b3a44f5bd12819953dc5fa3a7e6fa7a80db5ee853952"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2dee8e57f052ef5353cf608e0b4c871aee320dd1b87d351c28764fc0ca55f9f4"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8700f06d0ce6f128de3ccdbc1acaea1ee264d2caa9ca05daaf492fde7c2a7200"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1920d4ff15ce893210c1f0c0e9d19bfbecb7983c76b33f046c13a8ffbd570252"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:c1c76a1743432b4b60ab3358c937a3fe1341c828ae6194108a94c69028247f22"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:f7560358a6811e52e9c4d142d497f1a6e10103d3a6881f18d04dbce3729c0e2c"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-musllinux_1_1_ppc64le.whl", hash = "sha256:c8063cf17b19661471ecbdb3df1c84f24ad2e389e326ccaf89e3fb2484d8dd7e"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-musllinux_1_1_s390x.whl", hash = "sha256:cd6dbe0238f7743d0efe563ab46294f54f9bc8f4b9bcf57c3c666cc5bc9d1299"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:1249cbbf3d3b04902ff081ffbb33ce3377fa6e4c7356f759f3cd076cc138d020"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-win32.whl", hash = "sha256:6c409c0deba34f147f77efaa67b8e4bb83d2f11c8806405f76397ae5b8c0d1c9"},
    {file = "charset_normalizer-3.2.0-cp39-cp39-win_amd64.whl", hash = "sha256:7095f6fbfaa55defb6b733cfeb14efaae7a29f0b59d8cf213be4e7ca0b857b80"},
    {file = "charset_normalizer-3.2.0-py3-none-any.whl", hash = "sha256:8e098148dd37b4ce3baca71fb394c81dc5d9c7728c95df695d2dca218edf40e6"},
]

[[package]]
name = "click"
version = "8.1.6"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.7"
files = [
    {file = "click-8.1.6-py3-none-any.whl", hash = "sha256:fa244bb30b3b5ee2cae3da8f55c9e5e0c0e86093306301fb418eb9dc40fbded5"},
    {file = "click-8.1.6.tar.gz", hash = "sha256:48ee849951919527a045bfe3bf7baa8a959c423134e1a5b98c05c20ba75a1cbd"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "cmake"
version = "3.27.0"
description = "CMake is an open-source, cross-platform family of tools designed to build, test and package software"
optional = false
python-versions = "*"
files = [
    {file = "cmake-3.27.0-py2.py3-none-macosx_10_10_universal2.macosx_10_10_x86_64.macosx_11_0_arm64.macosx_11_0_universal2.whl", hash = "sha256:9ccab4cd93578d3c2df32e66b44b313b75a7484032645040431dc06a583ca4aa"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2010_i686.manylinux_2_12_i686.whl", hash = "sha256:199bfaefb752e82d8067aeee5d6a6e0414fe0d60e9a3fd08e95d537a97e0db16"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl", hash = "sha256:8745eff805f36762d3e8e904698b853cb4a9da8b4b07d1c12bcd1e1a6c4a1709"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:58a3f39d3d1bc897f05e531bfa676246a2b25d424c6a47e4b6bbc193fb560db7"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:b470ccd3f86cf19a63f6b221c9cceebcc58e32d3787d0d5f9f43d1d91a095090"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:35a8d397ce883e93b5e6561e2803ce9470df52283862264093c1078530f98189"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:1f38d87b2c65763a0113f4a6c652e6f4b5adf90b384c1e1d69e4f8a3104a57d6"},
    {file = "cmake-3.27.0-py2.py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:b9d5811954dcedcaa6c915c4a9bb6d64b55ac189e9cbc74be726307d9d084804"},
    {file = "cmake-3.27.0-py2.py3-none-musllinux_1_1_aarch64.whl", hash = "sha256:073e4f196d0888216e6794c08cd984ddabc108c0e4e66f48fbd7610d1e6d726d"},
    {file = "cmake-3.27.0-py2.py3-none-musllinux_1_1_i686.whl", hash = "sha256:e58e48643903e6fad76274337f9a4d3c575b8e21cd05c6214780b2c98bb0c706"},
    {file = "cmake-3.27.0-py2.py3-none-musllinux_1_1_ppc64le.whl", hash = "sha256:9740ed9f61a3bd8708a41cadd5c057c04f38e5b89bd773e369df2e210a1c55a3"},
    {file = "cmake-3.27.0-py2.py3-none-musllinux_1_1_s390x.whl", hash = "sha256:1b3189171665f5c8d748ae7fe10a29fff1ebeedeaef57b16f1ea54b1ec0fe514"},
    {file = "cmake-3.27.0-py2.py3-none-musllinux_1_1_x86_64.whl", hash = "sha256:c4c968c188e7518deb463a14e64f3a19f242c9dcf7f24e1dbcc1419690cd54e0"},
    {file = "cmake-3.27.0-py2.py3-none-win32.whl", hash = "sha256:5561aca62b65aac844f3931e74cfeb696e4534de145e3307bf942e735736541e"},
    {file = "cmake-3.27.0-py2.py3-none-win_amd64.whl", hash = "sha256:48be3afe62c9513a49be007896a4058fafec512cb1f269a50126da30aacad97f"},
    {file = "cmake-3.27.0-py2.py3-none-win_arm64.whl", hash = "sha256:6f46a170b0c9c552d52da4346534570f818195dfc4f1d0c03264e24cc348fc60"},
    {file = "cmake-3.27.0.tar.gz", hash = "sha256:d03f0a76a2b96805044ad1178b92aeeb5f695caa6776a32522bb5c430a55b4e8"},
]

[package.extras]
test = ["coverage (>=4.2)", "flake8 (>=3.0.4)", "path.py (>=11.5.0)", "pytest (>=3.0.3)", "pytest-cov (>=2.4.0)", "pytest-runner (>=2.9)", "pytest-virtualenv (>=1.7.0)", "scikit-build (>=0.10.0)", "setuptools (>=28.0.0)", "virtualenv (>=15.0.3)", "wheel"]

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "exceptiongroup"
version = "1.1.2"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
files = [
    {file = "exceptiongroup-1.1.2-py3-none-any.whl", hash = "sha256:e346e69d186172ca7cf029c8c1d16235aa0e04035e5750b4b95039e65204328f"},
    {file = "exceptiongroup-1.1.2.tar.gz", hash = "sha256:12c3e887d6485d16943a309616de20ae5582633e0a2eda17f4e10fd61c1e8af5"},
]

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "filelock"
version = "3.12.2"
description = "A platform independent file lock."
optional = false
python-versions = ">=3.7"
files = [
    {file = "filelock-3.12.2-py3-none-any.whl", hash = "sha256:cbb791cdea2a72f23da6ac5b5269ab0a0d161e9ef0100e653b69049a7706d1ec"},
    {file = "filelock-3.12.2.tar.gz", hash = "sha256:002740518d8aa59a26b0c76e10fb8c6e15eae825d34b6fdf670333fd7b938d81"},
]

[package.extras]
docs = ["furo (>=2023.5.20)", "sphinx (>=7.0.1)", "sphinx-autodoc-typehints (>=1.23,!=1.23.4)"]
testing = ["covdefaults (>=2.3)", "coverage (>=7.2.7)", "diff-cover (>=7.5)", "pytest (>=7.3.1)", "pytest-cov (>=4.1)", "pytest-mock (>=3.10)", "pytest-timeout (>=2.1)"]

[[package]]
name = "fire"
version = "0.5.0"
description = "A library for automatically generating command line interfaces."
optional = false
python-versions = "*"
files = [
    {file = "fire-0.5.0.tar.gz", hash = "sha256:a6b0d49e98c8963910021f92bba66f65ab440da2982b78eb1bbf95a0a34aacc6"},
]

[package.dependencies]
six = "*"
termcolor = "*"

[[package]]
name = "flake8"
version = "6.0.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.8.1"
files = [
    {file = "flake8-6.0.0-py2.py3-none-any.whl", hash = "sha256:3833794e27ff64ea4e9cf5d410082a8b97ff1a06c16aa3d2027339cd0f1195c7"},
    {file = "flake8-6.0.0.tar.gz", hash = "sha256:c61007e76655af75e6785a931f452915b371dc48f56efd765247c8fe68f2b181"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.10.0,<2.11.0"
pyflakes = ">=3.0.0,<3.1.0"

[[package]]
name = "idna"
version = "3.4"
description = "Internationalized Domain Names in Applications (IDNA)"
optional = false
python-versions = ">=3.5"
files = [
    {file = "idna-3.4-py3-none-any.whl", hash = "sha256:90b77e79eaa3eba6de819a0c442c0b4ceefc341a7a2ab77d7562bf49f425c5c2"},
    {file = "idna-3.4.tar.gz", hash = "sha256:814f528e8dead7d329833b91c5faa87d60bf71824cd12a7530b5526063d02cb4"},
]

[[package]]
name = "iniconfig"
version = "2.0.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.7"
files = [
    {file = "iniconfig-2.0.0-py3-none-any.whl", hash = "sha256:b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374"},
    {file = "iniconfig-2.0.0.tar.gz", hash = "sha256:2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"},
]

[[package]]
name = "jinja2"
version = "3.1.2"
description = "A very fast and expressive template engine."
optional = false
python-versions = ">=3.7"
files = [
    {file = "Jinja2-3.1.2-py3-none-any.whl", hash = "sha256:6088930bfe239f0e6710546ab9c19c9ef35e29792895fed6e6e31a023a182a61"},
    {file = "Jinja2-3.1.2.tar.gz", hash = "sha256:31351a702a408a9e7595a8fc6150fc3f43bb6bf7e319770cbc0db9df9437e852"},
]

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "lit"
version = "16.0.6"
description = "A Software Testing Tool"
optional = false
python-versions = "*"
files = [
    {file = "lit-16.0.6.tar.gz", hash = "sha256:84623c9c23b6b14763d637f4e63e6b721b3446ada40bf7001d8fee70b8e77a9a"},
]

[[package]]
name = "markupsafe"
version = "2.1.3"
description = "Safely add untrusted strings to HTML/XML markup."
optional = false
python-versions = ">=3.7"
files = [
    {file = "MarkupSafe-2.1.3-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:cd0f502fe016460680cd20aaa5a76d241d6f35a1c3350c474bac1273803893fa"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:e09031c87a1e51556fdcb46e5bd4f59dfb743061cf93c4d6831bf894f125eb57"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:68e78619a61ecf91e76aa3e6e8e33fc4894a2bebe93410754bd28fce0a8a4f9f"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:65c1a9bcdadc6c28eecee2c119465aebff8f7a584dd719facdd9e825ec61ab52"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:525808b8019e36eb524b8c68acdd63a37e75714eac50e988180b169d64480a00"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:962f82a3086483f5e5f64dbad880d31038b698494799b097bc59c2edf392fce6"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:aa7bd130efab1c280bed0f45501b7c8795f9fdbeb02e965371bbef3523627779"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:c9c804664ebe8f83a211cace637506669e7890fec1b4195b505c214e50dd4eb7"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-win32.whl", hash = "sha256:10bbfe99883db80bdbaff2dcf681dfc6533a614f700da1287707e8a5d78a8431"},
    {file = "MarkupSafe-2.1.3-cp310-cp310-win_amd64.whl", hash = "sha256:1577735524cdad32f9f694208aa75e422adba74f1baee7551620e43a3141f559"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:ad9e82fb8f09ade1c3e1b996a6337afac2b8b9e365f926f5a61aacc71adc5b3c"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:3c0fae6c3be832a0a0473ac912810b2877c8cb9d76ca48de1ed31e1c68386575"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b076b6226fb84157e3f7c971a47ff3a679d837cf338547532ab866c57930dbee"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bfce63a9e7834b12b87c64d6b155fdd9b3b96191b6bd334bf37db7ff1fe457f2"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:338ae27d6b8745585f87218a3f23f1512dbf52c26c28e322dbe54bcede54ccb9"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:e4dd52d80b8c83fdce44e12478ad2e85c64ea965e75d66dbeafb0a3e77308fcc"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:df0be2b576a7abbf737b1575f048c23fb1d769f267ec4358296f31c2479db8f9"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:5bbe06f8eeafd38e5d0a4894ffec89378b6c6a625ff57e3028921f8ff59318ac"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-win32.whl", hash = "sha256:dd15ff04ffd7e05ffcb7fe79f1b98041b8ea30ae9234aed2a9168b5797c3effb"},
    {file = "MarkupSafe-2.1.3-cp311-cp311-win_amd64.whl", hash = "sha256:134da1eca9ec0ae528110ccc9e48041e0828d79f24121a1a146161103c76e686"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:8e254ae696c88d98da6555f5ace2279cf7cd5b3f52be2b5cf97feafe883b58d2"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cb0932dc158471523c9637e807d9bfb93e06a95cbf010f1a38b98623b929ef2b"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9402b03f1a1b4dc4c19845e5c749e3ab82d5078d16a2a4c2cd2df62d57bb0707"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ca379055a47383d02a5400cb0d110cef0a776fc644cda797db0c5696cfd7e18e"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:b7ff0f54cb4ff66dd38bebd335a38e2c22c41a8ee45aa608efc890ac3e3931bc"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:c011a4149cfbcf9f03994ec2edffcb8b1dc2d2aede7ca243746df97a5d41ce48"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:56d9f2ecac662ca1611d183feb03a3fa4406469dafe241673d521dd5ae92a155"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-win32.whl", hash = "sha256:8758846a7e80910096950b67071243da3e5a20ed2546e6392603c096778d48e0"},
    {file = "MarkupSafe-2.1.3-cp37-cp37m-win_amd64.whl", hash = "sha256:787003c0ddb00500e49a10f2844fac87aa6ce977b90b0feaaf9de23c22508b24"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:2ef12179d3a291be237280175b542c07a36e7f60718296278d8593d21ca937d4"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:2c1b19b3aaacc6e57b7e25710ff571c24d6c3613a45e905b1fde04d691b98ee0"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8afafd99945ead6e075b973fefa56379c5b5c53fd8937dad92c662da5d8fd5ee"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8c41976a29d078bb235fea9b2ecd3da465df42a562910f9022f1a03107bd02be"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d080e0a5eb2529460b30190fcfcc4199bd7f827663f858a226a81bc27beaa97e"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:69c0f17e9f5a7afdf2cc9fb2d1ce6aabdb3bafb7f38017c0b77862bcec2bbad8"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:504b320cd4b7eff6f968eddf81127112db685e81f7e36e75f9f84f0df46041c3"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:42de32b22b6b804f42c5d98be4f7e5e977ecdd9ee9b660fda1a3edf03b11792d"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-win32.whl", hash = "sha256:ceb01949af7121f9fc39f7d27f91be8546f3fb112c608bc4029aef0bab86a2a5"},
    {file = "MarkupSafe-2.1.3-cp38-cp38-win_amd64.whl", hash = "sha256:1b40069d487e7edb2676d3fbdb2b0829ffa2cd63a2ec26c4938b2d34391b4ecc"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:8023faf4e01efadfa183e863fefde0046de576c6f14659e8782065bcece22198"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6b2b56950d93e41f33b4223ead100ea0fe11f8e6ee5f641eb753ce4b77a7042b"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9dcdfd0eaf283af041973bff14a2e143b8bd64e069f4c383416ecd79a81aab58"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:05fb21170423db021895e1ea1e1f3ab3adb85d1c2333cbc2310f2a26bc77272e"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:282c2cb35b5b673bbcadb33a585408104df04f14b2d9b01d4c345a3b92861c2c"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:ab4a0df41e7c16a1392727727e7998a467472d0ad65f3ad5e6e765015df08636"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:7ef3cb2ebbf91e330e3bb937efada0edd9003683db6b57bb108c4001f37a02ea"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:0a4e4a1aff6c7ac4cd55792abf96c915634c2b97e3cc1c7129578aa68ebd754e"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-win32.whl", hash = "sha256:fec21693218efe39aa7f8599346e90c705afa52c5b31ae019b2e57e8f6542bb2"},
    {file = "MarkupSafe-2.1.3-cp39-cp39-win_amd64.whl", hash = "sha256:3fd4abcb888d15a94f32b75d8fd18ee162ca0c064f35b11134be77050296d6ba"},
    {file = "MarkupSafe-2.1.3.tar.gz", hash = "sha256:af598ed32d6ae86f1b747b82783958b1a4ab8f617b06fe68795c7f026abbdcad"},
]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mpmath"
version = "1.3.0"
description = "Python library for arbitrary-precision floating-point arithmetic"
optional = false
python-versions = "*"
files = [
    {file = "mpmath-1.3.0-py3-none-any.whl", hash = "sha256:a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c"},
    {file = "mpmath-1.3.0.tar.gz", hash = "sha256:7a28eb2a9774d00c7bc92411c19a89209d5da7c4c9a9e227be8330a23a25b91f"},
]

[package.extras]
develop = ["codecov", "pycodestyle", "pytest (>=4.6)", "pytest-cov", "wheel"]
docs = ["sphinx"]
gmpy = ["gmpy2 (>=2.1.0a4)"]
tests = ["pytest (>=4.6)"]

[[package]]
name = "mypy-extensions"
version = "1.0.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.5"
files = [
    {file = "mypy_extensions-1.0.0-py3-none-any.whl", hash = "sha256:4392f6c0eb8a5668a69e23d168ffa70f0be9ccfd32b5cc2d26a34ae5b844552d"},
    {file = "mypy_extensions-1.0.0.tar.gz", hash = "sha256:75dbf8955dc00442a438fc4d0666508a9a97b6bd41aa2f0ffe9d2f2725af0782"},
]

[[package]]
name = "networkx"
version = "3.1"
description = "Python package for creating and manipulating graphs and networks"
optional = false
python-versions = ">=3.8"
files = [
    {file = "networkx-3.1-py3-none-any.whl", hash = "sha256:4f33f68cb2afcf86f28a45f43efc27a9386b535d567d2127f8f61d51dec58d36"},
    {file = "networkx-3.1.tar.gz", hash = "sha256:de346335408f84de0eada6ff9fafafff9bcda11f0a0dfaa931133debb146ab61"},
]

[package.extras]
default = ["matplotlib (>=3.4)", "numpy (>=1.20)", "pandas (>=1.3)", "scipy (>=1.8)"]
developer = ["mypy (>=1.1)", "pre-commit (>=3.2)"]
doc = ["nb2plots (>=0.6)", "numpydoc (>=1.5)", "pillow (>=9.4)", "pydata-sphinx-theme (>=0.13)", "sphinx (>=6.1)", "sphinx-gallery (>=0.12)", "texext (>=0.6.7)"]
extra = ["lxml (>=4.6)", "pydot (>=1.4.2)", "pygraphviz (>=1.10)", "sympy (>=1.10)"]
test = ["codecov (>=2.1)", "pytest (>=7.2)", "pytest-cov (>=4.0)"]

[[package]]
name = "numpy"
version = "1.25.1"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.9"
files = [
    {file = "numpy-1.25.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:77d339465dff3eb33c701430bcb9c325b60354698340229e1dff97745e6b3efa"},
    {file = "numpy-1.25.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:d736b75c3f2cb96843a5c7f8d8ccc414768d34b0a75f466c05f3a739b406f10b"},
    {file = "numpy-1.25.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4a90725800caeaa160732d6b31f3f843ebd45d6b5f3eec9e8cc287e30f2805bf"},
    {file = "numpy-1.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6c6c9261d21e617c6dc5eacba35cb68ec36bb72adcff0dee63f8fbc899362588"},
    {file = "numpy-1.25.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:0def91f8af6ec4bb94c370e38c575855bf1d0be8a8fbfba42ef9c073faf2cf19"},
    {file = "numpy-1.25.1-cp310-cp310-win32.whl", hash = "sha256:fd67b306320dcadea700a8f79b9e671e607f8696e98ec255915c0c6d6b818503"},
    {file = "numpy-1.25.1-cp310-cp310-win_amd64.whl", hash = "sha256:c1516db588987450b85595586605742879e50dcce923e8973f79529651545b57"},
    {file = "numpy-1.25.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:6b82655dd8efeea69dbf85d00fca40013d7f503212bc5259056244961268b66e"},
    {file = "numpy-1.25.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:e8f6049c4878cb16960fbbfb22105e49d13d752d4d8371b55110941fb3b17800"},
    {file = "numpy-1.25.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:41a56b70e8139884eccb2f733c2f7378af06c82304959e174f8e7370af112e09"},
    {file = "numpy-1.25.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d5154b1a25ec796b1aee12ac1b22f414f94752c5f94832f14d8d6c9ac40bcca6"},
    {file = "numpy-1.25.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:38eb6548bb91c421261b4805dc44def9ca1a6eef6444ce35ad1669c0f1a3fc5d"},
    {file = "numpy-1.25.1-cp311-cp311-win32.whl", hash = "sha256:791f409064d0a69dd20579345d852c59822c6aa087f23b07b1b4e28ff5880fcb"},
    {file = "numpy-1.25.1-cp311-cp311-win_amd64.whl", hash = "sha256:c40571fe966393b212689aa17e32ed905924120737194b5d5c1b20b9ed0fb171"},
    {file = "numpy-1.25.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:3d7abcdd85aea3e6cdddb59af2350c7ab1ed764397f8eec97a038ad244d2d105"},
    {file = "numpy-1.25.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:1a180429394f81c7933634ae49b37b472d343cccb5bb0c4a575ac8bbc433722f"},
    {file = "numpy-1.25.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d412c1697c3853c6fc3cb9751b4915859c7afe6a277c2bf00acf287d56c4e625"},
    {file = "numpy-1.25.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:20e1266411120a4f16fad8efa8e0454d21d00b8c7cee5b5ccad7565d95eb42dd"},
    {file = "numpy-1.25.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:f76aebc3358ade9eacf9bc2bb8ae589863a4f911611694103af05346637df1b7"},
    {file = "numpy-1.25.1-cp39-cp39-win32.whl", hash = "sha256:247d3ffdd7775bdf191f848be8d49100495114c82c2bd134e8d5d075fb386a1c"},
    {file = "numpy-1.25.1-cp39-cp39-win_amd64.whl", hash = "sha256:1d5d3c68e443c90b38fdf8ef40e60e2538a27548b39b12b73132456847f4b631"},
    {file = "numpy-1.25.1-pp39-pypy39_pp73-macosx_10_9_x86_64.whl", hash = "sha256:35a9527c977b924042170a0887de727cd84ff179e478481404c5dc66b4170009"},
    {file = "numpy-1.25.1-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0d3fe3dd0506a28493d82dc3cf254be8cd0d26f4008a417385cbf1ae95b54004"},
    {file = "numpy-1.25.1-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:012097b5b0d00a11070e8f2e261128c44157a8689f7dedcf35576e525893f4fe"},
    {file = "numpy-1.25.1.tar.gz", hash = "sha256:9a3a9f3a61480cc086117b426a8bd86869c213fc4072e606f01c4e4b66eb92bf"},
]

[[package]]
name = "nvidia-cublas-cu11"
version = "11.10.3.66"
description = "CUBLAS native runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cublas_cu11-11.10.3.66-py3-none-manylinux1_x86_64.whl", hash = "sha256:d32e4d75f94ddfb93ea0a5dda08389bcc65d8916a25cb9f37ac89edaeed3bded"},
    {file = "nvidia_cublas_cu11-11.10.3.66-py3-none-win_amd64.whl", hash = "sha256:8ac17ba6ade3ed56ab898a036f9ae0756f1e81052a317bf98f8c6d18dc3ae49e"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cuda-cupti-cu11"
version = "11.7.101"
description = "CUDA profiling tools runtime libs."
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cuda_cupti_cu11-11.7.101-py3-none-manylinux1_x86_64.whl", hash = "sha256:e0cfd9854e1f2edaa36ca20d21cd0bdd5dcfca4e3b9e130a082e05b33b6c5895"},
    {file = "nvidia_cuda_cupti_cu11-11.7.101-py3-none-win_amd64.whl", hash = "sha256:7cc5b8f91ae5e1389c3c0ad8866b3b016a175e827ea8f162a672990a402ab2b0"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cuda-nvrtc-cu11"
version = "11.7.99"
description = "NVRTC native runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cuda_nvrtc_cu11-11.7.99-2-py3-none-manylinux1_x86_64.whl", hash = "sha256:9f1562822ea264b7e34ed5930567e89242d266448e936b85bc97a3370feabb03"},
    {file = "nvidia_cuda_nvrtc_cu11-11.7.99-py3-none-manylinux1_x86_64.whl", hash = "sha256:f7d9610d9b7c331fa0da2d1b2858a4a8315e6d49765091d28711c8946e7425e7"},
    {file = "nvidia_cuda_nvrtc_cu11-11.7.99-py3-none-win_amd64.whl", hash = "sha256:f2effeb1309bdd1b3854fc9b17eaf997808f8b25968ce0c7070945c4265d64a3"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cuda-runtime-cu11"
version = "11.7.99"
description = "CUDA Runtime native Libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cuda_runtime_cu11-11.7.99-py3-none-manylinux1_x86_64.whl", hash = "sha256:cc768314ae58d2641f07eac350f40f99dcb35719c4faff4bc458a7cd2b119e31"},
    {file = "nvidia_cuda_runtime_cu11-11.7.99-py3-none-win_amd64.whl", hash = "sha256:bc77fa59a7679310df9d5c70ab13c4e34c64ae2124dd1efd7e5474b71be125c7"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cudnn-cu11"
version = "8.5.0.96"
description = "cuDNN runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cudnn_cu11-8.5.0.96-2-py3-none-manylinux1_x86_64.whl", hash = "sha256:402f40adfc6f418f9dae9ab402e773cfed9beae52333f6d86ae3107a1b9527e7"},
    {file = "nvidia_cudnn_cu11-8.5.0.96-py3-none-manylinux1_x86_64.whl", hash = "sha256:71f8111eb830879ff2836db3cccf03bbd735df9b0d17cd93761732ac50a8a108"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cufft-cu11"
version = "10.9.0.58"
description = "CUFFT native runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cufft_cu11-10.9.0.58-py3-none-manylinux1_x86_64.whl", hash = "sha256:222f9da70c80384632fd6035e4c3f16762d64ea7a843829cb278f98b3cb7dd81"},
    {file = "nvidia_cufft_cu11-10.9.0.58-py3-none-win_amd64.whl", hash = "sha256:c4d316f17c745ec9c728e30409612eaf77a8404c3733cdf6c9c1569634d1ca03"},
]

[[package]]
name = "nvidia-curand-cu11"
version = "10.2.10.91"
description = "CURAND native runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_curand_cu11-10.2.10.91-py3-none-manylinux1_x86_64.whl", hash = "sha256:eecb269c970fa599a2660c9232fa46aaccbf90d9170b96c462e13bcb4d129e2c"},
    {file = "nvidia_curand_cu11-10.2.10.91-py3-none-win_amd64.whl", hash = "sha256:f742052af0e1e75523bde18895a9ed016ecf1e5aa0ecddfcc3658fd11a1ff417"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cusolver-cu11"
version = "11.4.0.1"
description = "CUDA solver native runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cusolver_cu11-11.4.0.1-2-py3-none-manylinux1_x86_64.whl", hash = "sha256:72fa7261d755ed55c0074960df5904b65e2326f7adce364cbe4945063c1be412"},
    {file = "nvidia_cusolver_cu11-11.4.0.1-py3-none-manylinux1_x86_64.whl", hash = "sha256:700b781bfefd57d161443aff9ace1878584b93e0b2cfef3d6e9296d96febbf99"},
    {file = "nvidia_cusolver_cu11-11.4.0.1-py3-none-win_amd64.whl", hash = "sha256:00f70b256add65f8c1eb3b6a65308795a93e7740f6df9e273eccbba770d370c4"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-cusparse-cu11"
version = "11.7.4.91"
description = "CUSPARSE native runtime libraries"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_cusparse_cu11-11.7.4.91-py3-none-manylinux1_x86_64.whl", hash = "sha256:a3389de714db63321aa11fbec3919271f415ef19fda58aed7f2ede488c32733d"},
    {file = "nvidia_cusparse_cu11-11.7.4.91-py3-none-win_amd64.whl", hash = "sha256:304a01599534f5186a8ed1c3756879282c72c118bc77dd890dc1ff868cad25b9"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "nvidia-nccl-cu11"
version = "2.14.3"
description = "NVIDIA Collective Communication Library (NCCL) Runtime"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_nccl_cu11-2.14.3-py3-none-manylinux1_x86_64.whl", hash = "sha256:5e5534257d1284b8e825bc3a182c6f06acd6eb405e9f89d49340e98cd8f136eb"},
]

[[package]]
name = "nvidia-nvtx-cu11"
version = "11.7.91"
description = "NVIDIA Tools Extension"
optional = false
python-versions = ">=3"
files = [
    {file = "nvidia_nvtx_cu11-11.7.91-py3-none-manylinux1_x86_64.whl", hash = "sha256:b22c64eee426a62fc00952b507d6d29cf62b4c9df7a480fcc417e540e05fd5ac"},
    {file = "nvidia_nvtx_cu11-11.7.91-py3-none-win_amd64.whl", hash = "sha256:dfd7fcb2a91742513027d63a26b757f38dd8b07fecac282c4d132a9d373ff064"},
]

[package.dependencies]
setuptools = "*"
wheel = "*"

[[package]]
name = "opencv-python"
version = "4.8.0.74"
description = "Wrapper package for OpenCV python bindings."
optional = false
python-versions = ">=3.6"
files = [
    {file = "opencv-python-4.8.0.74.tar.gz", hash = "sha256:009e3ce356a0cd2d7423723e00a32fd3d3cc5bb5970ed27a9a1f8a8f221d1db5"},
    {file = "opencv_python-4.8.0.74-cp37-abi3-macosx_10_16_x86_64.whl", hash = "sha256:31d0d59fc8fdf703de4cec46c79b9f8d026fdde9d23d6e2e6a66809feeebbda9"},
    {file = "opencv_python-4.8.0.74-cp37-abi3-macosx_11_0_arm64.whl", hash = "sha256:66eadb5882ee56848b67f9fb57aadcaca2f4c9d9d00a0ef11043041925b51291"},
    {file = "opencv_python-4.8.0.74-cp37-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:038ba7075e55cb8e2846663ae970f0fb776a45b48ee69a887bf4ee15e2570083"},
    {file = "opencv_python-4.8.0.74-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:43dd0dfe331fb95767af581bf3b2781d7a72cf6560ddf2f55949fe547f3e5c9f"},
    {file = "opencv_python-4.8.0.74-cp37-abi3-win32.whl", hash = "sha256:458e5dc377f15fcf769d80314f3d885bd95457b1a2891bee67df2eb24a1d3a52"},
    {file = "opencv_python-4.8.0.74-cp37-abi3-win_amd64.whl", hash = "sha256:8fe0018d0056a5187c57120b6b3f6c3e706c13b45c48e54e86d245a9a16fac84"},
]

[package.dependencies]
numpy = [
    {version = ">=1.21.2", markers = "python_version >= \"3.10\""},
    {version = ">=1.21.4", markers = "python_version >= \"3.10\" and platform_system == \"Darwin\""},
    {version = ">=1.23.5", markers = "python_version >= \"3.11\""},
    {version = ">=1.19.3", markers = "python_version >= \"3.6\" and platform_system == \"Linux\" and platform_machine == \"aarch64\" or python_version >= \"3.9\""},
    {version = ">=1.17.0", markers = "python_version >= \"3.7\""},
    {version = ">=1.17.3", markers = "python_version >= \"3.8\""},
]

[[package]]
name = "packaging"
version = "23.1"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.7"
files = [
    {file = "packaging-23.1-py3-none-any.whl", hash = "sha256:994793af429502c4ea2ebf6bf664629d07c1a9fe974af92966e4b8d2df7edc61"},
    {file = "packaging-23.1.tar.gz", hash = "sha256:a392980d2b6cffa644431898be54b0045151319d1e7ec34f0cfed48767dd334f"},
]

[[package]]
name = "pathspec"
version = "0.11.1"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.7"
files = [
    {file = "pathspec-0.11.1-py3-none-any.whl", hash = "sha256:d8af70af76652554bd134c22b3e8a1cc46ed7d91edcdd721ef1a0c51a84a5293"},
    {file = "pathspec-0.11.1.tar.gz", hash = "sha256:2798de800fa92780e33acca925945e9a19a133b715067cf165b8866c15a31687"},
]

[[package]]
name = "pillow"
version = "9.5.0"
description = "Python Imaging Library (Fork)"
optional = false
python-versions = ">=3.7"
files = [
    {file = "Pillow-9.5.0-cp310-cp310-macosx_10_10_x86_64.whl", hash = "sha256:ace6ca218308447b9077c14ea4ef381ba0b67ee78d64046b3f19cf4e1139ad16"},
    {file = "Pillow-9.5.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:d3d403753c9d5adc04d4694d35cf0391f0f3d57c8e0030aac09d7678fa8030aa"},
    {file = "Pillow-9.5.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5ba1b81ee69573fe7124881762bb4cd2e4b6ed9dd28c9c60a632902fe8db8b38"},
    {file = "Pillow-9.5.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:fe7e1c262d3392afcf5071df9afa574544f28eac825284596ac6db56e6d11062"},
    {file = "Pillow-9.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8f36397bf3f7d7c6a3abdea815ecf6fd14e7fcd4418ab24bae01008d8d8ca15e"},
    {file = "Pillow-9.5.0-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:252a03f1bdddce077eff2354c3861bf437c892fb1832f75ce813ee94347aa9b5"},
    {file = "Pillow-9.5.0-cp310-cp310-manylinux_2_28_x86_64.whl", hash = "sha256:85ec677246533e27770b0de5cf0f9d6e4ec0c212a1f89dfc941b64b21226009d"},
    {file = "Pillow-9.5.0-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:b416f03d37d27290cb93597335a2f85ed446731200705b22bb927405320de903"},
    {file = "Pillow-9.5.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:1781a624c229cb35a2ac31cc4a77e28cafc8900733a864870c49bfeedacd106a"},
    {file = "Pillow-9.5.0-cp310-cp310-win32.whl", hash = "sha256:8507eda3cd0608a1f94f58c64817e83ec12fa93a9436938b191b80d9e4c0fc44"},
    {file = "Pillow-9.5.0-cp310-cp310-win_amd64.whl", hash = "sha256:d3c6b54e304c60c4181da1c9dadf83e4a54fd266a99c70ba646a9baa626819eb"},
    {file = "Pillow-9.5.0-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:7ec6f6ce99dab90b52da21cf0dc519e21095e332ff3b399a357c187b1a5eee32"},
    {file = "Pillow-9.5.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:560737e70cb9c6255d6dcba3de6578a9e2ec4b573659943a5e7e4af13f298f5c"},
    {file = "Pillow-9.5.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:96e88745a55b88a7c64fa49bceff363a1a27d9a64e04019c2281049444a571e3"},
    {file = "Pillow-9.5.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d9c206c29b46cfd343ea7cdfe1232443072bbb270d6a46f59c259460db76779a"},
    {file = "Pillow-9.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:cfcc2c53c06f2ccb8976fb5c71d448bdd0a07d26d8e07e321c103416444c7ad1"},
    {file = "Pillow-9.5.0-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:a0f9bb6c80e6efcde93ffc51256d5cfb2155ff8f78292f074f60f9e70b942d99"},
    {file = "Pillow-9.5.0-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:8d935f924bbab8f0a9a28404422da8af4904e36d5c33fc6f677e4c4485515625"},
    {file = "Pillow-9.5.0-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:fed1e1cf6a42577953abbe8e6cf2fe2f566daebde7c34724ec8803c4c0cda579"},
    {file = "Pillow-9.5.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c1170d6b195555644f0616fd6ed929dfcf6333b8675fcca044ae5ab110ded296"},
    {file = "Pillow-9.5.0-cp311-cp311-win32.whl", hash = "sha256:54f7102ad31a3de5666827526e248c3530b3a33539dbda27c6843d19d72644ec"},
    {file = "Pillow-9.5.0-cp311-cp311-win_amd64.whl", hash = "sha256:cfa4561277f677ecf651e2b22dc43e8f5368b74a25a8f7d1d4a3a243e573f2d4"},
    {file = "Pillow-9.5.0-cp311-cp311-win_arm64.whl", hash = "sha256:965e4a05ef364e7b973dd17fc765f42233415974d773e82144c9bbaaaea5d089"},
    {file = "Pillow-9.5.0-cp312-cp312-win32.whl", hash = "sha256:22baf0c3cf0c7f26e82d6e1adf118027afb325e703922c8dfc1d5d0156bb2eeb"},
    {file = "Pillow-9.5.0-cp312-cp312-win_amd64.whl", hash = "sha256:432b975c009cf649420615388561c0ce7cc31ce9b2e374db659ee4f7d57a1f8b"},
    {file = "Pillow-9.5.0-cp37-cp37m-macosx_10_10_x86_64.whl", hash = "sha256:5d4ebf8e1db4441a55c509c4baa7a0587a0210f7cd25fcfe74dbbce7a4bd1906"},
    {file = "Pillow-9.5.0-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:375f6e5ee9620a271acb6820b3d1e94ffa8e741c0601db4c0c4d3cb0a9c224bf"},
    {file = "Pillow-9.5.0-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:99eb6cafb6ba90e436684e08dad8be1637efb71c4f2180ee6b8f940739406e78"},
    {file = "Pillow-9.5.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2dfaaf10b6172697b9bceb9a3bd7b951819d1ca339a5ef294d1f1ac6d7f63270"},
    {file = "Pillow-9.5.0-cp37-cp37m-manylinux_2_28_aarch64.whl", hash = "sha256:763782b2e03e45e2c77d7779875f4432e25121ef002a41829d8868700d119392"},
    {file = "Pillow-9.5.0-cp37-cp37m-manylinux_2_28_x86_64.whl", hash = "sha256:35f6e77122a0c0762268216315bf239cf52b88865bba522999dc38f1c52b9b47"},
    {file = "Pillow-9.5.0-cp37-cp37m-win32.whl", hash = "sha256:aca1c196f407ec7cf04dcbb15d19a43c507a81f7ffc45b690899d6a76ac9fda7"},
    {file = "Pillow-9.5.0-cp37-cp37m-win_amd64.whl", hash = "sha256:322724c0032af6692456cd6ed554bb85f8149214d97398bb80613b04e33769f6"},
    {file = "Pillow-9.5.0-cp38-cp38-macosx_10_10_x86_64.whl", hash = "sha256:a0aa9417994d91301056f3d0038af1199eb7adc86e646a36b9e050b06f526597"},
    {file = "Pillow-9.5.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:f8286396b351785801a976b1e85ea88e937712ee2c3ac653710a4a57a8da5d9c"},
    {file = "Pillow-9.5.0-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c830a02caeb789633863b466b9de10c015bded434deb3ec87c768e53752ad22a"},
    {file = "Pillow-9.5.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:fbd359831c1657d69bb81f0db962905ee05e5e9451913b18b831febfe0519082"},
    {file = "Pillow-9.5.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f8fc330c3370a81bbf3f88557097d1ea26cd8b019d6433aa59f71195f5ddebbf"},
    {file = "Pillow-9.5.0-cp38-cp38-manylinux_2_28_aarch64.whl", hash = "sha256:7002d0797a3e4193c7cdee3198d7c14f92c0836d6b4a3f3046a64bd1ce8df2bf"},
    {file = "Pillow-9.5.0-cp38-cp38-manylinux_2_28_x86_64.whl", hash = "sha256:229e2c79c00e85989a34b5981a2b67aa079fd08c903f0aaead522a1d68d79e51"},
    {file = "Pillow-9.5.0-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:9adf58f5d64e474bed00d69bcd86ec4bcaa4123bfa70a65ce72e424bfb88ed96"},
    {file = "Pillow-9.5.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:662da1f3f89a302cc22faa9f14a262c2e3951f9dbc9617609a47521c69dd9f8f"},
    {file = "Pillow-9.5.0-cp38-cp38-win32.whl", hash = "sha256:6608ff3bf781eee0cd14d0901a2b9cc3d3834516532e3bd673a0a204dc8615fc"},
    {file = "Pillow-9.5.0-cp38-cp38-win_amd64.whl", hash = "sha256:e49eb4e95ff6fd7c0c402508894b1ef0e01b99a44320ba7d8ecbabefddcc5569"},
    {file = "Pillow-9.5.0-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:482877592e927fd263028c105b36272398e3e1be3269efda09f6ba21fd83ec66"},
    {file = "Pillow-9.5.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:3ded42b9ad70e5f1754fb7c2e2d6465a9c842e41d178f262e08b8c85ed8a1d8e"},
    {file = "Pillow-9.5.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c446d2245ba29820d405315083d55299a796695d747efceb5717a8b450324115"},
    {file = "Pillow-9.5.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8aca1152d93dcc27dc55395604dcfc55bed5f25ef4c98716a928bacba90d33a3"},
    {file = "Pillow-9.5.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:608488bdcbdb4ba7837461442b90ea6f3079397ddc968c31265c1e056964f1ef"},
    {file = "Pillow-9.5.0-cp39-cp39-manylinux_2_28_aarch64.whl", hash = "sha256:60037a8db8750e474af7ffc9faa9b5859e6c6d0a50e55c45576bf28be7419705"},
    {file = "Pillow-9.5.0-cp39-cp39-manylinux_2_28_x86_64.whl", hash = "sha256:07999f5834bdc404c442146942a2ecadd1cb6292f5229f4ed3b31e0a108746b1"},
    {file = "Pillow-9.5.0-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:a127ae76092974abfbfa38ca2d12cbeddcdeac0fb71f9627cc1135bedaf9d51a"},
    {file = "Pillow-9.5.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:489f8389261e5ed43ac8ff7b453162af39c3e8abd730af8363587ba64bb2e865"},
    {file = "Pillow-9.5.0-cp39-cp39-win32.whl", hash = "sha256:9b1af95c3a967bf1da94f253e56b6286b50af23392a886720f563c547e48e964"},
    {file = "Pillow-9.5.0-cp39-cp39-win_amd64.whl", hash = "sha256:77165c4a5e7d5a284f10a6efaa39a0ae8ba839da344f20b111d62cc932fa4e5d"},
    {file = "Pillow-9.5.0-pp38-pypy38_pp73-macosx_10_10_x86_64.whl", hash = "sha256:833b86a98e0ede388fa29363159c9b1a294b0905b5128baf01db683672f230f5"},
    {file = "Pillow-9.5.0-pp38-pypy38_pp73-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:aaf305d6d40bd9632198c766fb64f0c1a83ca5b667f16c1e79e1661ab5060140"},
    {file = "Pillow-9.5.0-pp38-pypy38_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0852ddb76d85f127c135b6dd1f0bb88dbb9ee990d2cd9aa9e28526c93e794fba"},
    {file = "Pillow-9.5.0-pp38-pypy38_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:91ec6fe47b5eb5a9968c79ad9ed78c342b1f97a091677ba0e012701add857829"},
    {file = "Pillow-9.5.0-pp38-pypy38_pp73-win_amd64.whl", hash = "sha256:cb841572862f629b99725ebaec3287fc6d275be9b14443ea746c1dd325053cbd"},
    {file = "Pillow-9.5.0-pp39-pypy39_pp73-macosx_10_10_x86_64.whl", hash = "sha256:c380b27d041209b849ed246b111b7c166ba36d7933ec6e41175fd15ab9eb1572"},
    {file = "Pillow-9.5.0-pp39-pypy39_pp73-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7c9af5a3b406a50e313467e3565fc99929717f780164fe6fbb7704edba0cebbe"},
    {file = "Pillow-9.5.0-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5671583eab84af046a397d6d0ba25343c00cd50bce03787948e0fff01d4fd9b1"},
    {file = "Pillow-9.5.0-pp39-pypy39_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:84a6f19ce086c1bf894644b43cd129702f781ba5751ca8572f08aa40ef0ab7b7"},
    {file = "Pillow-9.5.0-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:1e7723bd90ef94eda669a3c2c19d549874dd5badaeefabefd26053304abe5799"},
    {file = "Pillow-9.5.0.tar.gz", hash = "sha256:bf548479d336726d7a0eceb6e767e179fbde37833ae42794602631a070d630f1"},
]

[package.extras]
docs = ["furo", "olefile", "sphinx (>=2.4)", "sphinx-copybutton", "sphinx-inline-tabs", "sphinx-removed-in", "sphinxext-opengraph"]
tests = ["check-manifest", "coverage", "defusedxml", "markdown2", "olefile", "packaging", "pyroma", "pytest", "pytest-cov", "pytest-timeout"]

[[package]]
name = "platformdirs"
version = "3.9.1"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a \"user data dir\"."
optional = false
python-versions = ">=3.7"
files = [
    {file = "platformdirs-3.9.1-py3-none-any.whl", hash = "sha256:ad8291ae0ae5072f66c16945166cb11c63394c7a3ad1b1bc9828ca3162da8c2f"},
    {file = "platformdirs-3.9.1.tar.gz", hash = "sha256:1b42b450ad933e981d56e59f1b97495428c9bd60698baab9f3eb3d00d5822421"},
]

[package.extras]
docs = ["furo (>=2023.5.20)", "proselint (>=0.13)", "sphinx (>=7.0.1)", "sphinx-autodoc-typehints (>=1.23,!=1.23.4)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=7.3.1)", "pytest-cov (>=4.1)", "pytest-mock (>=3.10)"]

[[package]]
name = "pluggy"
version = "1.2.0"
description = "plugin and hook calling mechanisms for python"
optional = false
python-versions = ">=3.7"
files = [
    {file = "pluggy-1.2.0-py3-none-any.whl", hash = "sha256:c2fd55a7d7a3863cba1a013e4e2414658b1d07b6bc57b3919e0c63c9abb99849"},
    {file = "pluggy-1.2.0.tar.gz", hash = "sha256:d12f0c4b579b15f5e054301bb226ee85eeeba08ffec228092f8defbaa3a4c4b3"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["pytest", "pytest-benchmark"]

[[package]]
name = "pycodestyle"
version = "2.10.0"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pycodestyle-2.10.0-py2.py3-none-any.whl", hash = "sha256:8a4eaf0d0495c7395bdab3589ac2db602797d76207242c17d470186815706610"},
    {file = "pycodestyle-2.10.0.tar.gz", hash = "sha256:347187bdb476329d98f695c213d7295a846d1152ff4fe9bacb8a9590b8ee7053"},
]

[[package]]
name = "pyflakes"
version = "3.0.1"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pyflakes-3.0.1-py2.py3-none-any.whl", hash = "sha256:ec55bf7fe21fff7f1ad2f7da62363d749e2a470500eab1b555334b67aa1ef8cf"},
    {file = "pyflakes-3.0.1.tar.gz", hash = "sha256:ec8b276a6b60bd80defed25add7e439881c19e64850afd9b346283d4165fd0fd"},
]

[[package]]
name = "pytest"
version = "7.4.0"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.7"
files = [
    {file = "pytest-7.4.0-py3-none-any.whl", hash = "sha256:78bf16451a2eb8c7a2ea98e32dc119fd2aa758f1d5d66dbf0a59d69a3969df32"},
    {file = "pytest-7.4.0.tar.gz", hash = "sha256:b4bf8c45bd59934ed84001ad51e11b4ee40d40a1229d2c79f9c592b0a3f6bd8a"},
]

[package.dependencies]
colorama = {version = "*", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1.0.0rc8", markers = "python_version < \"3.11\""}
iniconfig = "*"
packaging = "*"
pluggy = ">=0.12,<2.0"
tomli = {version = ">=1.0.0", markers = "python_version < \"3.11\""}

[package.extras]
testing = ["argcomplete", "attrs (>=19.2.0)", "hypothesis (>=3.56)", "mock", "nose", "pygments (>=2.7.2)", "requests", "setuptools", "xmlschema"]

[[package]]
name = "requests"
version = "2.31.0"
description = "Python HTTP for Humans."
optional = false
python-versions = ">=3.7"
files = [
    {file = "requests-2.31.0-py3-none-any.whl", hash = "sha256:58cd2187c01e70e6e26505bca751777aa9f2ee0b7f4300988b709f44e013003f"},
    {file = "requests-2.31.0.tar.gz", hash = "sha256:942c5a758f98d790eaed1a29cb6eefc7ffb0d1cf7af05c3d2791656dbd6ad1e1"},
]

[package.dependencies]
certifi = ">=2017.4.17"
charset-normalizer = ">=2,<4"
idna = ">=2.5,<4"
urllib3 = ">=1.21.1,<3"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
use-chardet-on-py3 = ["chardet (>=3.0.2,<6)"]

[[package]]
name = "setuptools"
version = "68.0.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.7"
files = [
    {file = "setuptools-68.0.0-py3-none-any.whl", hash = "sha256:11e52c67415a381d10d6b462ced9cfb97066179f0e871399e006c4ab101fc85f"},
    {file = "setuptools-68.0.0.tar.gz", hash = "sha256:baf1fdb41c6da4cd2eae722e135500da913332ab3f2f5c7d33af9b492acb5235"},
]

[package.extras]
docs = ["furo", "jaraco.packaging (>=9)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-hoverxref (<2)", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (==0.8.3)", "sphinx-reredirects", "sphinxcontrib-towncrier"]
testing = ["build[virtualenv]", "filelock (>=3.4.0)", "flake8-2020", "ini2toml[lite] (>=0.9)", "jaraco.envs (>=2.2)", "jaraco.path (>=3.2.0)", "pip (>=19.1)", "pip-run (>=8.8)", "pytest (>=6)", "pytest-black (>=0.3.7)", "pytest-checkdocs (>=2.4)", "pytest-cov", "pytest-enabler (>=1.3)", "pytest-mypy (>=0.9.1)", "pytest-perf", "pytest-ruff", "pytest-timeout", "pytest-xdist", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel"]
testing-integration = ["build[virtualenv]", "filelock (>=3.4.0)", "jaraco.envs (>=2.2)", "jaraco.path (>=3.2.0)", "pytest", "pytest-enabler", "pytest-xdist", "tomli", "virtualenv (>=13.0.0)", "wheel"]

[[package]]
name = "six"
version = "1.16.0"
description = "Python 2 and 3 compatibility utilities"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*"
files = [
    {file = "six-1.16.0-py2.py3-none-any.whl", hash = "sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254"},
    {file = "six-1.16.0.tar.gz", hash = "sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926"},
]

[[package]]
name = "sympy"
version = "1.12"
description = "Computer algebra system (CAS) in Python"
optional = false
python-versions = ">=3.8"
files = [
    {file = "sympy-1.12-py3-none-any.whl", hash = "sha256:c3588cd4295d0c0f603d0f2ae780587e64e2efeedb3521e46b9bb1d08d184fa5"},
    {file = "sympy-1.12.tar.gz", hash = "sha256:ebf595c8dac3e0fdc4152c51878b498396ec7f30e7a914d6071e674d49420fb8"},
]

[package.dependencies]
mpmath = ">=0.19"

[[package]]
name = "termcolor"
version = "2.3.0"
description = "ANSI color formatting for output in terminal"
optional = false
python-versions = ">=3.7"
files = [
    {file = "termcolor-2.3.0-py3-none-any.whl", hash = "sha256:3afb05607b89aed0ffe25202399ee0867ad4d3cb4180d98aaf8eefa6a5f7d475"},
    {file = "termcolor-2.3.0.tar.gz", hash = "sha256:b5b08f68937f138fe92f6c089b99f1e2da0ae56c52b78bf7075fd95420fd9a5a"},
]

[package.extras]
tests = ["pytest", "pytest-cov"]

[[package]]
name = "tomli"
version = "2.0.1"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.7"
files = [
    {file = "tomli-2.0.1-py3-none-any.whl", hash = "sha256:939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc"},
    {file = "tomli-2.0.1.tar.gz", hash = "sha256:de526c12914f0c550d15924c62d72abc48d6fe7364aa87328337a31007fe8a4f"},
]

[[package]]
name = "torch"
version = "2.0.0"
description = "Tensors and Dynamic neural networks in Python with strong GPU acceleration"
optional = false
python-versions = ">=3.8.0"
files = [
    {file = "torch-2.0.0-1-cp310-cp310-manylinux2014_aarch64.whl", hash = "sha256:c9090bda7d2eeeecd74f51b721420dbeb44f838d4536cc1b284e879417e3064a"},
    {file = "torch-2.0.0-1-cp311-cp311-manylinux2014_aarch64.whl", hash = "sha256:bd42db2a48a20574d2c33489e120e9f32789c4dc13c514b0c44272972d14a2d7"},
    {file = "torch-2.0.0-1-cp38-cp38-manylinux2014_aarch64.whl", hash = "sha256:8969aa8375bcbc0c2993e7ede0a7f889df9515f18b9b548433f412affed478d9"},
    {file = "torch-2.0.0-1-cp39-cp39-manylinux2014_aarch64.whl", hash = "sha256:ab2da16567cb55b67ae39e32d520d68ec736191d88ac79526ca5874754c32203"},
    {file = "torch-2.0.0-cp310-cp310-manylinux1_x86_64.whl", hash = "sha256:7a9319a67294ef02459a19738bbfa8727bb5307b822dadd708bc2ccf6c901aca"},
    {file = "torch-2.0.0-cp310-cp310-manylinux2014_aarch64.whl", hash = "sha256:9f01fe1f6263f31bd04e1757946fd63ad531ae37f28bb2dbf66f5c826ee089f4"},
    {file = "torch-2.0.0-cp310-cp310-win_amd64.whl", hash = "sha256:527f4ae68df7b8301ee6b1158ca56350282ea633686537b30dbb5d7b4a52622a"},
    {file = "torch-2.0.0-cp310-none-macosx_10_9_x86_64.whl", hash = "sha256:ce9b5a49bd513dff7950a5a07d6e26594dd51989cee05ba388b03e8e366fd5d5"},
    {file = "torch-2.0.0-cp310-none-macosx_11_0_arm64.whl", hash = "sha256:53e1c33c6896583cdb9a583693e22e99266444c4a43392dddc562640d39e542b"},
    {file = "torch-2.0.0-cp311-cp311-manylinux1_x86_64.whl", hash = "sha256:09651bff72e439d004c991f15add0c397c66f98ab36fe60d5514b44e4da722e8"},
    {file = "torch-2.0.0-cp311-cp311-manylinux2014_aarch64.whl", hash = "sha256:d439aec349c98f12819e8564b8c54008e4613dd4428582af0e6e14c24ca85870"},
    {file = "torch-2.0.0-cp311-cp311-win_amd64.whl", hash = "sha256:2802f84f021907deee7e9470ed10c0e78af7457ac9a08a6cd7d55adef835fede"},
    {file = "torch-2.0.0-cp311-none-macosx_10_9_x86_64.whl", hash = "sha256:01858620f25f25e7a9ec4b547ff38e5e27c92d38ec4ccba9cfbfb31d7071ed9c"},
    {file = "torch-2.0.0-cp311-none-macosx_11_0_arm64.whl", hash = "sha256:9a2e53b5783ef5896a6af338b36d782f28e83c8ddfc2ac44b67b066d9d76f498"},
    {file = "torch-2.0.0-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:ec5fff2447663e369682838ff0f82187b4d846057ef4d119a8dea7772a0b17dd"},
    {file = "torch-2.0.0-cp38-cp38-manylinux2014_aarch64.whl", hash = "sha256:11b0384fe3c18c01b8fc5992e70fc519cde65e44c51cc87be1838c1803daf42f"},
    {file = "torch-2.0.0-cp38-cp38-win_amd64.whl", hash = "sha256:e54846aa63855298cfb1195487f032e413e7ac9cbfa978fda32354cc39551475"},
    {file = "torch-2.0.0-cp38-none-macosx_10_9_x86_64.whl", hash = "sha256:cc788cbbbbc6eb4c90e52c550efd067586c2693092cf367c135b34893a64ae78"},
    {file = "torch-2.0.0-cp38-none-macosx_11_0_arm64.whl", hash = "sha256:d292640f0fd72b7a31b2a6e3b635eb5065fcbedd4478f9cad1a1e7a9ec861d35"},
    {file = "torch-2.0.0-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:6befaad784004b7af357e3d87fa0863c1f642866291f12a4c2af2de435e8ac5c"},
    {file = "torch-2.0.0-cp39-cp39-manylinux2014_aarch64.whl", hash = "sha256:a83b26bd6ae36fbf5fee3d56973d9816e2002e8a3b7d9205531167c28aaa38a7"},
    {file = "torch-2.0.0-cp39-cp39-win_amd64.whl", hash = "sha256:c7e67195e1c3e33da53954b026e89a8e1ff3bc1aeb9eb32b677172d4a9b5dcbf"},
    {file = "torch-2.0.0-cp39-none-macosx_10_9_x86_64.whl", hash = "sha256:6e0b97beb037a165669c312591f242382e9109a240e20054d5a5782d9236cad0"},
    {file = "torch-2.0.0-cp39-none-macosx_11_0_arm64.whl", hash = "sha256:297a4919aff1c0f98a58ebe969200f71350a1d4d4f986dbfd60c02ffce780e99"},
]

[package.dependencies]
filelock = "*"
jinja2 = "*"
networkx = "*"
nvidia-cublas-cu11 = {version = "11.10.3.66", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cuda-cupti-cu11 = {version = "11.7.101", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cuda-nvrtc-cu11 = {version = "11.7.99", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cuda-runtime-cu11 = {version = "11.7.99", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cudnn-cu11 = {version = "8.5.0.96", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cufft-cu11 = {version = "10.9.0.58", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-curand-cu11 = {version = "10.2.10.91", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cusolver-cu11 = {version = "11.4.0.1", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-cusparse-cu11 = {version = "11.7.4.91", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-nccl-cu11 = {version = "2.14.3", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
nvidia-nvtx-cu11 = {version = "11.7.91", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
sympy = "*"
triton = {version = "2.0.0", markers = "platform_system == \"Linux\" and platform_machine == \"x86_64\""}
typing-extensions = "*"

[package.extras]
opt-einsum = ["opt-einsum (>=3.3)"]

[[package]]
name = "torchvision"
version = "0.15.1"
description = "image and video datasets and models for torch deep learning"
optional = false
python-versions = ">=3.8"
files = [
    {file = "torchvision-0.15.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:bc10d48e9a60d006d0c1b48dea87f1ec9b63d856737d592f7c5c44cd87f3f4b7"},
    {file = "torchvision-0.15.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:3708d3410fdcaf6280e358cda9de2a4ab06cc0b4c0fd9aeeac550ec2563a887e"},
    {file = "torchvision-0.15.1-cp310-cp310-manylinux1_x86_64.whl", hash = "sha256:d4de10c837f1493c1c54344388e300a06c96914c6cc55fcb2527c21f2f010bbd"},
    {file = "torchvision-0.15.1-cp310-cp310-manylinux2014_aarch64.whl", hash = "sha256:b82fcc5abc9b5c96495c76596a1573025cc1e09d97d2d6fda717c44b9ca45881"},
    {file = "torchvision-0.15.1-cp310-cp310-win_amd64.whl", hash = "sha256:c84e97d8cc4fe167d87adad0a2a6424cff90544365545b20669bc50e6ea46875"},
    {file = "torchvision-0.15.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:97b90eb3b7333a31d049c4ccfd1064361e8491874959d38f466af64d67418cef"},
    {file = "torchvision-0.15.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:6b60e1c839ae2a071befbba69b17468d67feafdf576e90ff9645bfbee998de17"},
    {file = "torchvision-0.15.1-cp311-cp311-manylinux1_x86_64.whl", hash = "sha256:13f71a3372d9168b01481a754ebaa171207f3dc455bf2fd86906c69222443738"},
    {file = "torchvision-0.15.1-cp311-cp311-manylinux2014_aarch64.whl", hash = "sha256:b2e8394726009090b40f6cc3a95cc878cc011dfac3d8e7a6060c79213d360880"},
    {file = "torchvision-0.15.1-cp311-cp311-win_amd64.whl", hash = "sha256:2852f501189483187ce9eb0ccd01b3f4f0918d29057e4a18b3cce8dad9a8a964"},
    {file = "torchvision-0.15.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:e5861baaeea87d19b6fd7d131e11a4a6bd17be14234c490a259bb360775e9520"},
    {file = "torchvision-0.15.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:e714f362b9d8217cf4d68509b679ebc9ddf128cfe80f6c1def8e3f8a18466e75"},
    {file = "torchvision-0.15.1-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:43624accad1e47f16824be4db37ad678dd89326ad90b69c9c6363eeb22b9467e"},
    {file = "torchvision-0.15.1-cp38-cp38-manylinux2014_aarch64.whl", hash = "sha256:7fe9b0cd3311b0db9e6d45ffab594ced06418fa4e2aa15eb2e60d55e5c51135c"},
    {file = "torchvision-0.15.1-cp38-cp38-win_amd64.whl", hash = "sha256:b45324ea4911a23a4b00b5a15cdbe36d47f93137206dab9f8c606d81b69dd3a7"},
    {file = "torchvision-0.15.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:1dfdec7c7df967330bba3341a781e0c047d4e0163e67164a9918500362bf7d91"},
    {file = "torchvision-0.15.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:c153710186cec0338d4fff411459a57ddbc8504436123ca73b3f0bdc26ff918c"},
    {file = "torchvision-0.15.1-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:ff4e650aa601f32ab97bce06704868dd2baad69ca4d454fa1f0012a51199f2bc"},
    {file = "torchvision-0.15.1-cp39-cp39-manylinux2014_aarch64.whl", hash = "sha256:e9b4bb2a15849391df0415d2f76dd36e6528e4253f7b69322b7a0d682535544b"},
    {file = "torchvision-0.15.1-cp39-cp39-win_amd64.whl", hash = "sha256:21e6beb69e77ef6575c4fdd0ab332b96e8a7f144eee0d333acff469c827a4b5e"},
]

[package.dependencies]
numpy = "*"
pillow = ">=5.3.0,<8.3.dev0 || >=8.4.dev0"
requests = "*"
torch = "2.0.0"

[package.extras]
scipy = ["scipy"]

[[package]]
name = "triton"
version = "2.0.0"
description = "A language and compiler for custom Deep Learning operations"
optional = false
python-versions = "*"
files = [
    {file = "triton-2.0.0-1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:38806ee9663f4b0f7cd64790e96c579374089e58f49aac4a6608121aa55e2505"},
    {file = "triton-2.0.0-1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:226941c7b8595219ddef59a1fdb821e8c744289a132415ddd584facedeb475b1"},
    {file = "triton-2.0.0-1-cp36-cp36m-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4c9fc8c89874bc48eb7e7b2107a9b8d2c0bf139778637be5bfccb09191685cfd"},
    {file = "triton-2.0.0-1-cp37-cp37m-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:d2684b6a60b9f174f447f36f933e9a45f31db96cb723723ecd2dcfd1c57b778b"},
    {file = "triton-2.0.0-1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:9d4978298b74fcf59a75fe71e535c092b023088933b2f1df933ec32615e4beef"},
    {file = "triton-2.0.0-1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:74f118c12b437fb2ca25e1a04759173b517582fcf4c7be11913316c764213656"},
    {file = "triton-2.0.0-1-pp37-pypy37_pp73-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:9618815a8da1d9157514f08f855d9e9ff92e329cd81c0305003eb9ec25cc5add"},
    {file = "triton-2.0.0-1-pp38-pypy38_pp73-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:1aca3303629cd3136375b82cb9921727f804e47ebee27b2677fef23005c3851a"},
    {file = "triton-2.0.0-1-pp39-pypy39_pp73-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e3e13aa8b527c9b642e3a9defcc0fbd8ffbe1c80d8ac8c15a01692478dc64d8a"},
    {file = "triton-2.0.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8f05a7e64e4ca0565535e3d5d3405d7e49f9d308505bb7773d21fb26a4c008c2"},
    {file = "triton-2.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bb4b99ca3c6844066e516658541d876c28a5f6e3a852286bbc97ad57134827fd"},
    {file = "triton-2.0.0-cp36-cp36m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47b4d70dc92fb40af553b4460492c31dc7d3a114a979ffb7a5cdedb7eb546c08"},
    {file = "triton-2.0.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fedce6a381901b1547e0e7e1f2546e4f65dca6d91e2d8a7305a2d1f5551895be"},
    {file = "triton-2.0.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:75834f27926eab6c7f00ce73aaf1ab5bfb9bec6eb57ab7c0bfc0a23fac803b4c"},
    {file = "triton-2.0.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0117722f8c2b579cd429e0bee80f7731ae05f63fe8e9414acd9a679885fcbf42"},
    {file = "triton-2.0.0-pp37-pypy37_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bcd9be5d0c2e45d2b7e6ddc6da20112b6862d69741576f9c3dbaf941d745ecae"},
    {file = "triton-2.0.0-pp38-pypy38_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:42a0d2c3fc2eab4ba71384f2e785fbfd47aa41ae05fa58bf12cb31dcbd0aeceb"},
    {file = "triton-2.0.0-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:52c47b72c72693198163ece9d90a721299e4fb3b8e24fd13141e384ad952724f"},
]

[package.dependencies]
cmake = "*"
filelock = "*"
lit = "*"
torch = "*"

[package.extras]
tests = ["autopep8", "flake8", "isort", "numpy", "pytest", "scipy (>=1.7.1)"]
tutorials = ["matplotlib", "pandas", "tabulate"]

[[package]]
name = "typing-extensions"
version = "4.7.1"
description = "Backported and Experimental Type Hints for Python 3.7+"
optional = false
python-versions = ">=3.7"
files = [
    {file = "typing_extensions-4.7.1-py3-none-any.whl", hash = "sha256:440d5dd3af93b060174bf433bccd69b0babc3b15b1a8dca43789fd7f61514b36"},
    {file = "typing_extensions-4.7.1.tar.gz", hash = "sha256:b75ddc264f0ba5615db7ba217daeb99701ad295353c45f9e95963337ceeeffb2"},
]

[[package]]
name = "urllib3"
version = "2.0.4"
description = "HTTP library with thread-safe connection pooling, file post, and more."
optional = false
python-versions = ">=3.7"
files = [
    {file = "urllib3-2.0.4-py3-none-any.whl", hash = "sha256:de7df1803967d2c2a98e4b11bb7d6bd9210474c46e8a0401514e3a42a75ebde4"},
    {file = "urllib3-2.0.4.tar.gz", hash = "sha256:8d22f86aae8ef5e410d4f539fde9ce6b2113a001bb4d189e0aed70642d602b11"},
]

[package.extras]
brotli = ["brotli (>=1.0.9)", "brotlicffi (>=0.8.0)"]
secure = ["certifi", "cryptography (>=1.9)", "idna (>=2.0.0)", "pyopenssl (>=17.1.0)", "urllib3-secure-extra"]
socks = ["pysocks (>=1.5.6,!=1.5.7,<2.0)"]
zstd = ["zstandard (>=0.18.0)"]

[[package]]
name = "wheel"
version = "0.41.0"
description = "A built-package format for Python"
optional = false
python-versions = ">=3.7"
files = [
    {file = "wheel-0.41.0-py3-none-any.whl", hash = "sha256:7e9be3bbd0078f6147d82ed9ed957e323e7708f57e134743d2edef3a7b7972a9"},
    {file = "wheel-0.41.0.tar.gz", hash = "sha256:55a0f0a5a84869bce5ba775abfd9c462e3a6b1b7b7ec69d72c0b83d673a5114d"},
]

[package.extras]
test = ["pytest (>=6.0.0)", "setuptools (>=65)"]

[metadata]
lock-version = "2.0"
python-versions = "^3.10"
content-hash = "dea2bf70866c9f2c0132956dc54c8f22f4676533f693f7cc881441b6693d111d"


-----------------------

/pyproject.toml:
-----------------------

[tool.poetry]
name = "simple-lama-inpainting"
version = "0.1.2"
description = ""
authors = ["enesmsahin <enessahin@outlook.com>"]
readme = "README.md"
packages = [{include = "simple_lama_inpainting"}]

[tool.poetry.dependencies]
python = "^3.10"
numpy = "^1.24.3"
opencv-python = "^4.8.0.74"
pillow = "^9.5.0"
torch = ">=1.13.1, !=2.0.1"
torchvision = ">=0.14.1"
fire = "^0.5.0"

[tool.poetry.scripts]
simple_lama = "simple_lama_inpainting.cli:lama_cli"

[tool.poetry.group.test.dependencies]
pytest = "^7.4.0"


[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
flake8 = "^6.0.0"
black = "^23.7.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


-----------------------

/simple_lama_inpainting/__init__.py:
-----------------------

from simple_lama_inpainting.models.model import SimpleLama

__all__ = ['SimpleLama',]


-----------------------

/simple_lama_inpainting/cli.py:
-----------------------

from simple_lama_inpainting.models.model import SimpleLama
from PIL import Image
from pathlib import Path
import fire


def main(image_path: str, mask_path: str, out_path: str | None = None):
    """Apply lama inpainting using given image and mask.

    Args:
        img_path (str): Path to input image (RGB)
        mask_path (str): Path to input mask (Binary 1-CH Image.
                        Pixels with value 255 will be inpainted)
        out_path (str, optional): Optional output imaga path.
                        If not provided it will be saved to the same
                            path as input image.
                        Defaults to None.
    """
    image_path = Path(image_path)
    mask_path = Path(mask_path)

    img = Image.open(image_path).convert("RGB")
    mask = Image.open(mask_path).convert("L")

    assert img.mode == "RGB" and mask.mode == "L"

    lama = SimpleLama()
    result = lama(img, mask)
    if out_path is None:
        out_path = image_path.with_stem(image_path.stem + "_out")

    Path.mkdir(Path(out_path).parent, exist_ok=True, parents=True)
    result.save(out_path)
    print(f"Inpainted image is saved to {out_path}")


def lama_cli():
    fire.Fire(main)


if __name__ == "__main__":
    fire.Fire(main)


-----------------------

/simple_lama_inpainting/models/__init__.py:
-----------------------

/simple_lama_inpainting/models/model.py:
-----------------------

import os
import torch
import numpy as np
from PIL import Image
from simple_lama_inpainting.utils.util import prepare_img_and_mask, download_model

LAMA_MODEL_URL = os.environ.get(
    "LAMA_MODEL_URL",
    "https://github.com/enesmsahin/simple-lama-inpainting/releases/download/v0.1.0/big-lama.pt",  # noqa
)


class SimpleLama:
    def __init__(
        self,
        device: torch.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        ),
    ) -> None:
        if os.environ.get("LAMA_MODEL"):
            model_path = os.environ.get("LAMA_MODEL")
            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"lama torchscript model not found: {model_path}"
                )
        else:
            model_path = download_model(LAMA_MODEL_URL)

        self.model = torch.jit.load(model_path, map_location=device)
        self.model.eval()
        self.model.to(device)
        self.device = device

    def __call__(self, image: Image.Image | np.ndarray, mask: Image.Image | np.ndarray):
        image, mask = prepare_img_and_mask(image, mask, self.device)

        with torch.inference_mode():
            inpainted = self.model(image, mask)

            cur_res = inpainted[0].permute(1, 2, 0).detach().cpu().numpy()
            cur_res = np.clip(cur_res * 255, 0, 255).astype(np.uint8)

            cur_res = Image.fromarray(cur_res)
            return cur_res


-----------------------

/simple_lama_inpainting/utils/__init__.py:
-----------------------

/simple_lama_inpainting/utils/util.py:
-----------------------

import os
import sys
import torch
import numpy as np
import cv2
from PIL import Image
from torch.hub import download_url_to_file, get_dir
from urllib.parse import urlparse


# Source https://github.com/advimman/lama
def get_image(image):
    if isinstance(image, Image.Image):
        img = np.array(image)
    elif isinstance(image, np.ndarray):
        img = image.copy()
    else:
        raise Exception("Input image should be either PIL Image or numpy array!")

    if img.ndim == 3:
        img = np.transpose(img, (2, 0, 1))  # chw
    elif img.ndim == 2:
        img = img[np.newaxis, ...]

    assert img.ndim == 3

    img = img.astype(np.float32) / 255
    return img


def ceil_modulo(x, mod):
    if x % mod == 0:
        return x
    return (x // mod + 1) * mod


def scale_image(img, factor, interpolation=cv2.INTER_AREA):
    if img.shape[0] == 1:
        img = img[0]
    else:
        img = np.transpose(img, (1, 2, 0))

    img = cv2.resize(img, dsize=None, fx=factor, fy=factor, interpolation=interpolation)

    if img.ndim == 2:
        img = img[None, ...]
    else:
        img = np.transpose(img, (2, 0, 1))
    return img


def pad_img_to_modulo(img, mod):
    channels, height, width = img.shape
    out_height = ceil_modulo(height, mod)
    out_width = ceil_modulo(width, mod)
    return np.pad(
        img,
        ((0, 0), (0, out_height - height), (0, out_width - width)),
        mode="symmetric",
    )


def prepare_img_and_mask(image, mask, device, pad_out_to_modulo=8, scale_factor=None):
    out_image = get_image(image)
    out_mask = get_image(mask)

    if scale_factor is not None:
        out_image = scale_image(out_image, scale_factor)
        out_mask = scale_image(out_mask, scale_factor, interpolation=cv2.INTER_NEAREST)

    if pad_out_to_modulo is not None and pad_out_to_modulo > 1:
        out_image = pad_img_to_modulo(out_image, pad_out_to_modulo)
        out_mask = pad_img_to_modulo(out_mask, pad_out_to_modulo)

    out_image = torch.from_numpy(out_image).unsqueeze(0).to(device)
    out_mask = torch.from_numpy(out_mask).unsqueeze(0).to(device)

    out_mask = (out_mask > 0) * 1

    return out_image, out_mask


# Source: https://github.com/Sanster/lama-cleaner/blob/6cfc7c30f1d6428c02e21d153048381923498cac/lama_cleaner/helper.py # noqa
def get_cache_path_by_url(url):
    parts = urlparse(url)
    hub_dir = get_dir()
    model_dir = os.path.join(hub_dir, "checkpoints")
    if not os.path.isdir(model_dir):
        os.makedirs(os.path.join(model_dir, "hub", "checkpoints"))
    filename = os.path.basename(parts.path)
    cached_file = os.path.join(model_dir, filename)
    return cached_file


def download_model(url):
    cached_file = get_cache_path_by_url(url)
    if not os.path.exists(cached_file):
        sys.stderr.write('Downloading: "{}" to {}\n'.format(url, cached_file))
        hash_prefix = None
        download_url_to_file(url, cached_file, hash_prefix, progress=True)
    return cached_file


-----------------------

/tests/__init__.py:
-----------------------

/tests/conftest.py:
-----------------------

import pytest
import torch
from pathlib import Path
from PIL import Image
from typing import Tuple
from simple_lama_inpainting import SimpleLama


@pytest.fixture(scope="session")
def image_paths() -> Tuple[Path, Path, Path]:
    image_path = Path(__file__).parent / "data" / "image_1.png"
    mask_path = Path(__file__).parent / "data" / "mask_1.png"
    out_path = Path(__file__).parent / "data" / "out_1.png"

    return image_path, mask_path, out_path


@pytest.fixture(scope="session")
def images(
    image_paths: Tuple[Path, Path, Path]
) -> Tuple[Image.Image, Image.Image, Image.Image]:
    image = Image.open(image_paths[0])
    mask = Image.open(image_paths[1])
    out = Image.open(image_paths[2])

    return image, mask, out


@pytest.fixture(scope="session")
def device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


@pytest.fixture(scope="session")
def simple_lama(device) -> SimpleLama:
    return SimpleLama(device)


-----------------------

/tests/test_lama.py:
-----------------------

from typing import Tuple
from PIL import Image
from pathlib import Path
import numpy as np
from simple_lama_inpainting import SimpleLama
import subprocess
import tempfile


def test_lama(
    images: Tuple[Image.Image, Image.Image, Image.Image], simple_lama: SimpleLama
):
    out = simple_lama(*images[:-1])
    np.testing.assert_array_equal(np.array(out), np.array(images[-1]))


def test_lama_cli(image_paths: Tuple[Path, Path, Path]):
    temp_dir = tempfile.TemporaryDirectory()
    out_file_path = Path(temp_dir.name) / "tmp_out.png"
    subprocess.run(
        ["simple_lama", str(image_paths[0]), str(image_paths[1]), str(out_file_path)],
        check=True,
    )
    np.testing.assert_array_equal(
        np.array(Image.open(out_file_path)), np.array(Image.open(image_paths[-1]))
    )
    temp_dir.cleanup()