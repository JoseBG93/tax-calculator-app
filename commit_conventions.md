
## 🚀 **feat**: New Capabilities
Used for changes that add a new capability to the software. The user who benefits from this new capability could be:

- **End-user** interacting with a website or app *(e.g., adding a new "dark mode" button)*
- **Developer** consuming your API
- **System administrator** using a new command in a CLI tool

### 📋 Examples of Non-UI Features:
- **API Development**: Adding a new endpoint for clients to consume
  ```
  feat(api): add /users/{id}/profile endpoint
  ```
- **CLI Tools**: Introducing a new command or flag
  ```
  feat(cli): add --json flag to the list command
  ```
- **Libraries/SDKs**: Implementing a new public function for other developers to use
  ```
  feat(core): export new calculateTaxes() function
  ```
- **Backend Logic**: Adding a new data export option that runs in the background
  ```
  feat(exports): implement CSV export for user data
  ```

---

## 🐛 **fix**: Bug Fixes
Bug fix or code behavior correction

---

## 🔧 **refactor**: Code Structure Improvements
Used for any change to the source code that improves its internal structure without changing its external behavior. It allows you to reorganize your code to make it cleaner, more efficient, or easier to understand, but without fixing a bug or adding a new feature.

### 📝 Common Examples:
- Renaming variables or functions for better clarity
- Splitting a large, complex function into smaller, single-purpose functions
- Removing duplicate or dead code
- Reorganizing files and directory structures
- Applying a design pattern to improve code architecture

### ⚖️ How 'refactor' differs from other types:
- **refactor vs. perf**: If your change is exclusively aimed at improving performance, it's better to use `perf`. If the performance gain is a side effect of a larger code cleanup, `refactor` is more appropriate.

---

## 📚 **docs**: Documentation
Documentation only

---

## 🎨 **style**: Formatting
Formatting only, no logic/behavior. For example, CSS.

---

## 🧪 **test**: Testing
Add/modify tests

---

## 🏗️ **build**: Build Process
Used for changes that affect the project's build process or its external dependencies, for example, when adding, removing or updating dependencies in files like `package.json`, `requirements.txt` or `pom.xml`.

---

## 🔄 **ci**: Continuous Integration
For Continuous Integration. Reserved for changes made to your continuous integration configuration files and scripts, for example, when editing files like `.github/workflows/main.yml`, `.travis.yml` or `Jenkinsfile`. These changes affect the automation pipeline (testing, deploying), not the application's source code or its build requirements.

### 🛠️ Typical Components of a CI configuration:
- Definition of build, test and deploy steps
- Specification of environments or containers
- Setting up dependencies and secrets
- Configuration of triggers *(e.g., when on pull request or on commit)*
- Artifact storage or deployment destinations

---

## ⚡ **perf**: Performance
Performance improvement

---

## 🧹 **chore**: Maintenance Tasks
Used for routine maintenance tasks and other changes that don't modify the application's source code or its tests.

### 📋 Common Examples:
- Updating build tools or task runners *(like Webpack, Gulp, etc.)*
- Managing project configuration files *(like .gitignore, .editorconfig, or Prettier settings)*
- Adding or modifying scripts that assist with development or deployment
- General repository maintenance, like cleaning up files or restructuring directories

### ⚖️ How 'chore' differs from other types:
- **chore vs. build**: `build` is for changes that affect external dependencies the application needs to run *(e.g., updating a library in package.json)*. `chore` is for changes to the tools that support the development process itself.
- **chore vs. ci**: `ci` is specifically for changes to the Continuous Integration pipeline *(e.g., editing a GitHub Actions workflow)*. `chore` covers other miscellaneous developer-facing tasks.
- **chore vs. refactor**: `refactor` is for restructuring existing application code without changing its behavior. `chore` is for tasks that don't touch the production source code at all.