# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_all, collect_data

block_cipher = None

base_path = os.path.abspath(SPECPATH)

# Collect all data and binaries for key ML packages
datas = []
binaries = []
hiddenimports = []

for pkg in ['torch', 'transformers', 'tokenizers', 'regex', 'sentencepiece', 'safetensors', 'scipy', 'numpy', 'huggingface_hub', 'beartype']:
    try:
        pkg_datas, pkg_binaries, pkg_hidden = collect_all(pkg)
        datas.extend(pkg_datas)
        binaries.extend(pkg_binaries)
        hiddenimports.extend(pkg_hidden)
    except Exception:
        pass

# Add pocket_tts static files
datas.append((os.path.join(base_path, 'pocket_tts', 'static'), 'pocket_tts/static'))

# Add config files if they exist
for config_dir in ['configs', os.path.join(base_path, 'pocket_tts', 'utils', 'configs')]:
    if os.path.exists(config_dir):
        datas.append((config_dir, 'configs'))

a = Analysis(
    ['pocket-tts-launcher.py'],
    pathex=[base_path],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports + [
        'pocket_tts.main',
        'pocket_tts.data.audio',
        'pocket_tts.models.tts_model',
        'pocket_tts.models.flow_lm',
        'pocket_tts.models.mimi',
        'pocket_tts.conditioners.text',
        'pocket_tts.modules.mimi_transformer',
        'pocket_tts.modules.mlp',
        'pocket_tts.modules.conv',
        'pocket_tts.modules.resample',
        'pocket_tts.modules.seanet',
        'pocket_tts.modules.dummy_quantizer',
        'pocket_tts.modules.stateful_module',
        'pocket_tts.modules.layer_scale',
        'pocket_tts.modules.rope',
        'pocket_tts.modules.transformer',
        'pocket_tts.quantization',
        'pocket_tts.utils.config',
        'pocket_tts.utils.utils',
        'pocket_tts.utils.logging_utils',
        'pocket_tts.utils.weights_loading',
        'pocket_tts.default_parameters',
        'fastapi',
        'uvicorn',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'starlette',
        'pydantic',
        'pydantic.deprecated',
        'pydantic_core',
        'typing_extensions',
        'packaging',
        'filelock',
        'requests',
        'tqdm',
        'yaml',
        'jinja2',
        'markupsafe',
        'soundfile',
        'soundfile._soundfiledata',
        '_soundfile_data',
        'scipy.io.wavfile',
        'scipy.signal',
        'scipy.special',
        'scipy.special._cdflib',
        'torchaudio',
        'torch.nn',
        'torch.nn.functional',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tensorboard', 'torch.utils.tensorboard'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PocketTTS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(base_path, 'pocket_tts', 'static', 'favicon.ico'),
)
