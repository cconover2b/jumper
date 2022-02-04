**** Don’t forget to add each username as a collaborator under Settings and Collaborators ****

## **Cloning**

- Navigate to the repo you would like to clone.

[https://github.com/cconover2b/jumper.git](https://github.com/cconover2b/jumper.git)

```python
git clone https://github.com/cconover2b/jumper.git
```

- Now, move into that folder that was just created from the repository

```python
cd jumper
```

## **Add and Commit to Git**

- Add a line to the README.md just for testing

```python
git add README.md
```

```python
git commit -m "Added a line"
```

### If you get an auth error like this:

```python
Author identity unknown

** Please tell me who you are.

Run

git config --global user.email "you@example.com"

git config --global user.name "Your Name"

to set your account's default identity.

Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'growthemp@GrowthPC2.(none)')
```

- Here is what to do:

```python
git config --global user.email "youremail@gmail.com"
```

```python
git config --global user.name "Craig Conover"
```

- Now continue with the commit

```python
git commit -m "Added a line of code."
```

- I had to login with my browser and then it worked perfectly.

## **To remove as file from cached on Git**

- if you have added a file or committed a file, to get it from being tracked so you can add it to another branch or something like that.

```python
git rm --cached <file>

# Here is my Example:

git rm --cached test2.py
```

## **Add a New Branch and Add, Commit, and Push**

- Add a branch

```python
git branch cconover2b
```

- Switch to that branch

```python
git checkout cconover2b
```

- Now Add files

```python
git add test.py
```

```python
git commit -m "Added a test file"
```

- For your first push on a new branch, you must add an upstream

```python
git push -u https://github.com/cconover2b/jumper.git
```

- After you have pushed once you can just use git push going forward

```python
git push
```

## **Pull Requests**

- On Github.com click "Compare & pull request"
- Add any comments you want and click Pull request

## **Merge**

- On GitHub.com click on "Pull Requests"
- Click on the ones that are open
- If there are no conflicts, then press "Merge pull request"
- Then "Confirm merge"

### With Conflicts

- [Git merge conflicts | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)