# stoepsel - a simple plug-in system for python

Stoepsel (pronounce ʃtœpsl̩) is an attempt to create a simple (as in
minimalistic) but flexible and powerful plugin system for python.

Stoepsel gives you the ability to develop flexible and scalable applications.
It doesn't matter if you want to build a UI or console program.
You just need to deploy a plugin class to register your application part.

Plugins can use other plugins. Therefore, you can register objects or functions
in a model tree where other plugins can find them.
To make this as safe as possible, a simple dependency resolving algorithm is
implemented.
Plugins are registered by their name and a version. They also can define
dependencies that have to be resolved. (more on that later)

# using stoepsel

## installing stoepsel

you can install stoepsel by using pip

    python3 -m pip install stoepsel

Or just initialize a virtualenv and run setup.py

    python3 -m venv env
    source env/bin/activate
    python3 setup.py install


## running a stoepsel application

A simple stoepsel application can look like this:

    import logging
    from stoepsel import PluginManager

    def main(args):
        logging.basicConfig(level=logging.DEBUG)

        # instanciate PluginManager
        pm = PluginManager()
        # find main and execute it
        pm.get_item(PluginManager.PGM_MAIN)()

        return 0

    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))

In this case, stoepsel will look for folder named 'plugins' and read any .py-
file into its registry.
One file has to register (see below) the term '__main__' or simply
PluginManager.PGM_MAIN. This is the entry point for our application.

## stoepsel configuration

It's possible to configure stoepsel and stoepsel plugins. Therefore, you can
give a dictionary to PluginManager constructor which at least consists of
'plugin_path', a string which tells a directory where stoepsel looks for
plugins and 'plugin_config' where plugin configuration can be stored.


    config = {}
    config['plugin_path'] = 'simple_plugins'
    config['plugin_config'] = {}

    pm = PluginManager(config)

You could also put this into a json based (or other) config file

    with open('config.json') as fp:
        config = json.load(fp)
        pm = PluginManager(config)

## creating a plugin

a plugin is a class which derives from stoepsel.Plugin. It needs to deploy
static information about it's name, version and dependencies.
Additionally, you need to define a variable `export` which points to your
plugin class

    from stoepsel import Plugin

    class MyPlugin(Plugin):
        name = 'simple_plugin'
        version = '0.0.1'
        dependencies = []

        def setup(self):
            self.register(self.PGM_MAIN,self.main)

        def main(self):
            print('Running around...')

    export = MyPlugin

## registering objects

you can register objects by utilizing the Plugin method 'register'

    def setup(self):
        self.register('myapp/plugins/plg1/sayhi', self.sayhi)

    def sayhi(self):
        print('hello world')

## using registered objects

to use registered objects you fave to find them via get_item method

    def setup(self):
        sayhi = self.get_item('myapp/plugins/plg1/sayhi')
        if sayhi is not None:
            sayhi()

## configuration

The configuration of the PluginManager is also set into the model tree
so you can get it by utilizing get_item

    self.get_item('config:plugin_config/myplugin')

this can be useful to create configuration dialogues. To make it easier
there is a property config set:

    print(self.config['plugin_config/mypath'])

Also a list of plugins can be read by using 'plugins:' as path or just

   print(self.plugins)



# TODOs

- pattern matching for dependency version control
- get rid of the `export =` in plugn file
- find plugins recursively
