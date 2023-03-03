import launch

if not launch.is_installed("html2text"):
    launch.run_pip("install html2text", "requirements for Library Notes")
