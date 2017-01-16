# Boilerplate for Bottle on Azure with Continuous Deployment

## About

This repository contains a sample [bottle][] application for [Azure Web Apps][],
which automatically deploys a new version as soon as the corresponding GitHub
repository is updated (a.k.a. continuous deployment, see also [Azure App Service][]).

The code is based on the Bottle template in the Azure Marketplace
as described on this [Azure documentation page][] (2015-06-24).

_Update_ : see https://docs.microsoft.com/en-us/azure/app-service-web/web-sites-python-create-deploy-bottle-app


## Usage

Three steps to start from scratch:

1. Create your project and run the Web App locally
2. Add the project to GitHub
3. Connect your GitHub project to an Azure Web App

### Create your project and run locally

The easiest way to get started is download the current ZIP file at
<https://github.com/ernstbaslerpartner/bottle-azure-boilerplate/archive/master.zip>. Unzip
the file, rename the folder to `mynewprojectname`.

In order to develop and test the Web App on your machine, you need to create a
[virtual environment for your Python project][venv] and install the necessary
requirements, see also [Azure documentation page][] for details. Sounds scary,
but it is done within a couple of seconds. Then you can run the site locally.

Here is a summary of the necessary steps (for Windows):

    # Get the code
    wget https://github.com/ernstbaslerpartner/bottle-azure-boilerplate/archive/master.zip
    unzip master.zip
    mv bottle-azure-boilerplate-master mynewprojectname
    cd mynewprojectname
    
    # Create virtual environment and run the site locally 
    python -m virtualenv env
    env\Scripts\pip install -r requirements.txt # for Unix, change slashes accordingly
    env\Scripts\python app.py --debug           # for Unix, change slashes accordingly

The development server now runs on <http://localhost:5555/>.

At this point, you may want to edit the source code and this Readme file.

### Add the project to GitHub

If you have one the Github desktop clients ([Mac](https://mac.github.com/) or
[Win](https://windows.github.com/)) installed, just drag-n-drop the folder to
the desktop client. The folder is now locally registered as a git
repository. You then have to publish the repository to GitHub by clicking on
the "Publish" button.

Alternatively, you can
[add the folder to Github with the command line][GitHub command line].

### Create an Azure Web App and connect it to your GitHub project 

Now you are 5 easy steps away from your live website:

1. Log into [Azure Portal][] and create a "Web App". Wait until the app is
   available, which may take a couple of seconds.
2. Click on the created Web App and then click the tile "Deployment".
3. Click on "Choose Source" and then "Github".
4. Authorize Azure to access your GitHub account.
5. Choose the repository. Wait until the initial version is deployed.

Now, as soon as you push a change to your GitHub repository, the change will be
deployed automatically to the Azure site.

A demo site can be found at
<http://bottle-azure-boilerplate.azurewebsites.net/> (this site may take a
second to load as it runs on a free plan).

## App Settings

If you have configuration settings such as API keys, you don't want to put them
in your GitHub repository. Instead, define an "App Setting" variable
`MY_CONFIG` in your Azure Web App, see also
[this video on application settings][appsettings]. In the code, we assume that
the value of the app setting is a JSON string.

## Webjobs

An Azure Web App can also have [background webjobs][].

You can initialize a webjob called `process_queue`as follows (assuming Windows
shell and [Azure CLI][] installed):

    > cd App_Data\jobs\triggered\process_queue\
    > zip run.zip run.py
    > azure site job upload process_queue triggered run.zip sbbdelaybot
    info:    Executing command site job upload
    + Getting locations
    + Getting sites
    + Getting site information
    + Uploading new WebJob
    + Getting WebJob
    info:    WebJob process_queue has been uploaded
    info:    site job upload command OK

You can also create your webjob manually on Azure Portal.

After this one-time initialization, any changes to run.py will be automatically
deployed as soon as you commit your changes to GitHub.

Please note: A triggered webjob apparently needs a Web-App with standard tier
and configured to be "Always On".

### Changes to the original code

There was one problem with the original code from the Marketplace: static files
were not served on Azure, only on the development server. I suspect there is a
problem with web.config (in my case for 2.7). However, I could not figure out
the problem, see [my comment here][comment]. As a quick fix, I moved the static
file handler to `route.py`.

## Author

* original code by the PTVS team (source code repository unknown)
* changes by Stephan Heuel, [@ping13](http://ping13.net)


[bottle]: http://bottlepy.org

[Azure documentation page]: https://azure.microsoft.com/en-us/documentation/articles/web-sites-python-create-deploy-bottle-app

[Azure Portal]: http://portal.azure.com

[comment]: https://azure.microsoft.com/en-us/documentation/articles/web-sites-python-create-deploy-bottle-app/#comment-2094572524
[GitHub command line]: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

[venv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/

[Azure App Service]: https://azure.microsoft.com/en-us/documentation/articles/web-sites-publish-source-control/

[appsettings]: http://azure.microsoft.com/en-us/documentation/videos/configuration-and-app-settings-of-azure-web-sites/

[background webjobs]: https://azure.microsoft.com/en-us/documentation/articles/web-sites-create-web-jobs/#CreateContinuous

[Azure CLI]: https://azure.microsoft.com/en-us/documentation/articles/xplat-cli/

[Azure Web Apps]: http://azure.microsoft.com/en-us/services/app-service/web/
