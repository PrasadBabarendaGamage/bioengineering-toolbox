# Github FAQ

## [Adding badges to repositories](https://github.com/Naereen/badges)

## [Renaming repositories and updating remote paths of clones](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/renaming-a-repository)
```bash
# Get the remote origin url of the old repository.
git remote get-url origin
# This will produce output like e.g.:
# git@github.com:UOA-Heart-Mechanics-Research/heart_metadata.git

# Set the new remote origin url to the new repository name.
git remote set-url origin git@github.com:UOA-Heart-Mechanics-Research/heart-metadata.git
```
