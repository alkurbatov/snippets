((python-mode
  (eval . (python-black-on-save-mode))
  (eval add-hook 'before-save-hook 'py-isort-before-save)))
