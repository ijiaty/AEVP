# How to put this ZIP into GitHub without using a token

When command-line authentication feels difficult, use the GitHub web page.

## Simple web upload flow

1. Open the GitHub repository page.
2. Press **Add file**.
3. Choose **Upload files**.
4. Drag and drop the files from this ZIP.
5. Press **Commit changes**.

This avoids `git push` and avoids creating a Personal Access Token.

## If the repository is empty

If the repository is empty, upload the contents of this ZIP directly.
Do not upload the outer `AEVP_complete` folder unless you want that folder to
appear inside the repository.

## Command-line flow, only when comfortable

```bash
git clone https://github.com/ijiaty/AEVP.git
cd AEVP
unzip ~/Downloads/aevp_complete_root_contents.zip
python3 run.py
python3 -m pip install -r requirements.txt
python3 -m pytest
git add .
git commit -m "Add minimal AEVP prediction and scoring pipeline"
git push -u origin main
```

GitHub no longer accepts the normal account password for command-line push.
Use the web upload flow if token creation is stressful.
