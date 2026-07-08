"""Generate a CMake presets file from a template file."""

import json
import sys

def main() -> None:
  templates = load_preset_templates()
  presets = dict()
  presets["
  sys.exit(0)


def load_preset_template() -> dict:
  with open("CMakePresetsTemplate.json", mode="r", encoding="utf-8") as template_file:
    templates = json.load(template_file)
  return templates


def copy_basic_preset_data(templates: dict) -> dict:
  presets = templates
  del presets["buildPresets"]
  del presets["testPresets"]
  del presets["packagePresets"]
  del presets["workflowPresets"]
  return presets
  
if __name__ == "__main__":
  main()
else:
  sys.exit("This is an application, not an importable module.")
