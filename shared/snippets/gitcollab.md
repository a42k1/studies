# Git Collaboration Guide

<https://www.w3schools.com/git/>
This is an ai answer please check wiki above for a more trusted source.

## Essential Git Workflow

### Initial Setup

```bash
# Configure your identity (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Clone a repository
git clone <repository-url>
cd <repository-name>
```

## Core Daily Commands

### 1. **Check Status & Updates**

```bash
# See what's changed locally
git status

# Get latest changes from remote
git fetch origin

# Pull changes from main branch
git pull origin main
```

### 2. **Branch Workflow** (Most Important!)

```bash
# Create and switch to new branch
git checkout -b feature/your-feature-name

# List all branches
git branch -a

# Switch branches
git checkout main
```

### 3. **Making Changes**

```bash
# Stage specific files
git add file1.js file2.css

# Stage all changes
git add .

# Commit with message
git commit -m "Add user authentication feature"

# Push to remote
git push origin feature/your-feature-name
```

## Best Practices

### **Commit Messages**

- Use present tense: "Add feature" not "Added feature"
- Be descriptive but concise
- Format: `Type: Brief description`

```bash
git commit -m "Fix: Resolve login timeout issue"
git commit -m "Feat: Add password reset functionality"
git commit -m "Docs: Update API documentation"
```

### **Branch Naming Conventions**

```
feature/add-user-profile
bugfix/fix-login-error
hotfix/critical-security-patch
refactor/optimize-database-queries
```

### **Pull Request Workflow**

1. Create feature branch from `main`
2. Make changes and commit regularly
3. Push branch to remote
4. Create Pull Request (PR) on GitHub/GitLab
5. Request code review
6. Address feedback
7. Merge after approval

## Common Scenarios

### **Syncing with Main Branch**

```bash
# Update your feature branch with latest main
git checkout main
git pull origin main
git checkout feature/your-feature
git merge main
# Resolve conflicts if any, then commit
```

### **Handling Merge Conflicts**

```bash
# When conflict occurs during merge/pull
# 1. Open conflicted files (VS Code shows conflicts clearly)
# 2. Choose changes or merge manually
# 3. Remove conflict markers (<<<<, ====, >>>>)
# 4. Stage resolved files
git add resolved-file.js
git commit -m "Resolve merge conflicts"
```

### **Undoing Changes**

```bash
# Discard uncommitted changes in file
git checkout -- filename.js

# Unstage a file
git reset HEAD filename.js

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) - CAREFUL!
git reset --hard HEAD~1
```

### **Stashing Changes**

```bash
# Save work in progress temporarily
git stash

# List stashes
git stash list

# Apply most recent stash
git stash pop

# Apply specific stash
git stash apply stash@{0}
```

## Team Collaboration Rules

### **Never Do This:**

- ❌ Don't push directly to `main`/`master`
- ❌ Don't force push to shared branches (`git push --force`)
- ❌ Don't commit sensitive data (passwords, API keys)
- ❌ Don't commit large binary files without Git LFS

### **Always Do This:**

- ✅ Pull before starting work
- ✅ Commit often with clear messages
- ✅ Create feature branches
- ✅ Review your changes before committing
- ✅ Keep commits atomic (one logical change per commit)

## Viewing History

```bash
# See commit history
git log --oneline --graph --all

# See changes in last commit
git show

# See who changed what in a file
git blame filename.js
```

## Useful Aliases (Optional)

```bash
# Add shortcuts
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm "commit -m"

# Now you can use: git st, git co, etc.
```

## Typical Day Flow

```bash
# Morning: Start work
git checkout main
git pull origin main
git checkout -b feature/new-widget

# During day: Make changes
git add .
git commit -m "Feat: Add widget component"
git push origin feature/new-widget

# Evening: Sync with team updates
git checkout main
git pull origin main
git checkout feature/new-widget
git merge main
git push origin feature/new-widget

# Create PR on GitHub/GitLab
# After PR approval: Delete local branch
git checkout main
git branch -d feature/new-widget
```

## When You Need Advanced Commands

**Rebase** (alternative to merge, use when team agrees):

```bash
git rebase main  # Cleaner history but riskier
```

**Cherry-pick** (copy specific commit):

```bash
git cherry-pick <commit-hash>
```

## Quick Reference Cheat Sheet

| Command                    | Purpose                   |
| -------------------------- | ------------------------- |
| `git status`               | Check current changes     |
| `git pull`                 | Get latest from remote    |
| `git checkout -b <branch>` | Create new branch         |
| `git add .`                | Stage all changes         |
| `git commit -m "msg"`      | Commit changes            |
| `git push origin <branch>` | Push to remote            |
| `git merge <branch>`       | Merge branch into current |
| `git stash`                | Temporarily save changes  |
| `git log --oneline`        | View commit history       |

---

_This covers 95% of daily Git usage in teams. Start with the basics and add advanced techniques as needed!_
