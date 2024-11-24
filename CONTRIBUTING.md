# LaTeX Project Setup & Contribution Guide

## 1. Setting Up VSCode with LaTeX

1. Download and install [Visual Studio Code](https://code.visualstudio.com/)
2. Install the LaTeX Workshop extension:
   - Open VSCode
   - Click the Extensions icon in the sidebar (or press `Ctrl+Shift+X`)
   - Search for "LaTeX Workshop" and install

### [Additional Requirements](https://github.com/James-Yu/latex-workshop/wiki/Install)
Install a TeX distribution. LiveTeX is recommended.


## 2. How to Contribute

### Forking the repository
1. Fork the repository:
   - Go to https://github.com/koskja/mff-mat
   - Click the "Fork" button in the top-right corner
   - Select your account as the destination

2. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/mff-mat
   ```

3. Add the original repository as upstream:
   ```bash
   git remote add upstream https://github.com/koskja/mff-mat
   ```

### Making Changes
1. Before starting work, sync your fork with upstream:
   ```bash
   git fetch upstream
   git merge upstream/main
   ```
This makes changes from the original repository available in your fork.

2. The actual work
 - Copy an assignment file and rename it to some variant of your name.
 - Make your changes.

4. Commit your changes:
   - In VSCode, click the Source Control icon in the sidebar (or press `Ctrl+Shift+G`)
   - Add all files you want to commit using the `+` button
   - Enter any commit message
   - Click the checkmark to commit

5. Push your changes:
   ```bash
   git push origin main
   ```

6. Create a Pull Request:
   - Go to the upstream repository on GitHub
   - Click "Pull Requests"
   - Click "New Pull Request"
   - Select your branch
   - Click "Create Pull Request"
   - Add a description of your changes
   - Click "Create Pull Request"
