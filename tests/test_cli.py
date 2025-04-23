import subprocess
import os
import shutil

def test_cli_runs(tmp_path):
    """Test basic CLI execution and output generation."""
    out_dir = tmp_path / "uml_out"
    result = subprocess.run(
        ["python", "-m", "pyumlify.cli", "--root", "tests/fixtures", "--output", str(out_dir)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert out_dir.exists()
    assert any(f.name.endswith(".puml") for f in out_dir.iterdir())
