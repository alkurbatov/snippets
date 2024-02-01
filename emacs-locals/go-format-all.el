((nil . ((format-all-formatters . (("Go" gci gofumpt)))))
 (go-ts-mode
  (eval add-hook 'before-save-hook #'format-all-buffer nil 'local)))
