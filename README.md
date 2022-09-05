<h1 align="center">👨‍💻 Epitech Criterion Actions</h1>

<p align="center">Simple GitHub action for Criterion unit tests at Epitech</p>

<p align="center">
<a href="./LICENCE"><img alt="License" src="https://img.shields.io/badge/License-GPLv3-blue.svg" /><a>
<a href="https://github.com/MaximePremont/EpitechCriterionActions/issues"><img alt="issues" src="https://badgen.net/github/issues/MaximePremont/EpitechCriterionActions" /></a>
<a href="https://github.com/MaximePremont/EpitechCriterionActions"><img alt="PRs" src="https://badgen.net/github/prs/MaximePremont/EpitechCriterionActions" /></a>
<a href="https://github.com/MaximePremont/EpitechCriterionActions"><img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" /></a>
<a href="https://github.com/MaximePremont/EpitechCriterionActions/network/members"><img alt="forks" src="https://badgen.net/github/forks/MaximePremont/EpitechCriterionActions" /></a>
<a href="https://github.com/MaximePremont/EpitechCriterionActions"><img alt="stars" src="https://badgen.net/github/stars/MaximePremont/EpitechCriterionActions" /></a>
</p>

## 🔍 Description

Epitech Criterion Actions is a GitHub action that will automatically launch the unit tests create with [Criterion](https://criterion.readthedocs.io/en/master/index.html) in the same way as the Epitech autocorrector. One the action is incorporated into the project, it will start when chages are sent to the main branch of the project. The results are formatted and sent to a special branch named "epitech-criterion-action" ( [see branch on example project](https://github.com/MaximePremont/EpitechCriterionActions_Example/tree/epitech-criterion-actions) )

## 💻 Example

### An example project has been created: [MaximePremont/EpitechCriterionActions_Example](https://github.com/MaximePremont/EpitechCriterionActions_Example)
![Example](./example.png?raw=true "Example")
<p align="center">README.md of epitech-criterion-actions branch</p>

## ⚠️ Requirements

The criterion unit tests and the project must be organized as indecated in the epitech unit tests documentation.
#### The main points are :
* Have your Makefile at the root of the repository
* Have a "tests_run" rule that compiles the tests with `-lcriterion` and `--coverage`
* The test executable must be called "unit_tests"
* The test executable must not be deleted when calling "tests_run" in the makefile
> Do not hesitate to take a look at [the sample project](https://github.com/MaximePremont/EpitechCriterionActions_Example) to see how to correctly build your project and Makefile.

## 📝 Usage

Create a `.github/workflows/epitechcriterionactions.yaml` workflow file in your project repository :
```yaml
on:
  push:
    branches:
      - main
      - master
jobs:
  execute:
    runs-on: ubuntu-20.04
    steps:
      - uses: MaximePremont/EpitechCriterionActions@master
```

## 📄 Support

If you have any questions or problems, you can [create an issue](https://github.com/MaximePremont/EpitechCriterionActions/issues).

## 💡 Contributing


Do you have the slightest idea or do you want to develop the project? **Feel free to contribute !** For this a [contribution guide](./CONTRIBUTING.md) is available.


## 👤 You are an Epitech student ?  

Do not hesitate to use this GitHub Action for your projects and your reviews !

#### Don't forget to leave a star if the project was useful to you :star:


> [Epitech Criterion Actions](https://github.com/MaximePremont/EpitechCriterionActions) by [Maxime Premont](http://github.com/MaximePremont)


