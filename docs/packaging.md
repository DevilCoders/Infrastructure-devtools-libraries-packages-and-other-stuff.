# Desktop Packaging Guide

This guide walks through producing a Windows ``.exe`` build of Infra Manager
Studio using [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/). The
utility wraps PyInstaller with a friendly UI that captures the configuration.

## Prerequisites

- Python 3.10+
- A virtual environment with the project installed via ``pip install .[dev]``
- ``auto-py-to-exe`` (installed automatically with the ``dev`` extras)

## Steps

1. Launch the interface:

   ```bash
   python -m auto_py_to_exe
   ```

2. In the *Script* picker, choose ``launch_infra_manager.py`` from the project
   root. The helper imports the packaged application and delegates to
   ``infra_manager.app.main``.

3. Select **Onefile** if you want a single executable, or **Onedir** to inspect
   the unpacked files.

4. Switch to the *Advanced* tab and add the following to **Additional Hooks** to
   ensure the embedded Qt resources ship with the bundle:

   ```text
   --collect-all infra_manager.ui
   ```

5. Click **Convert .py to .exe**. PyInstaller will build the executable. The
   output directory is displayed at the bottom of the auto-py-to-exe window.

## Troubleshooting

- **Missing Qt platform plugin** – ensure ``PyQt6`` is bundled. Using the
  provided ``pyproject.toml`` and ``launch_infra_manager.py`` script guarantees
  PyInstaller detects the dependency.
- **Stylesheet not applied** – confirm the ``--collect-all infra_manager.ui``
  flag is present so the neon stylesheet is shipped alongside the bytecode.
- **Antivirus false positives** – rebuild using the **Onedir** mode and manually
  inspect/sign the executable before distribution.

With these steps the neon-themed UI, high-DPI settings, and AI-ready panels will
all be preserved inside a Windows-friendly ``.exe``. For automated build
pipelines, you can export the auto-py-to-exe configuration JSON and check it
into version control.
