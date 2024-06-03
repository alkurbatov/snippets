((nil
  (format-all-formatters
   ("Go" goimports
         gofumpt)))
 (go-ts-mode
  (eval add-hook 'before-save-hook #'format-all-buffer nil 'local)))
