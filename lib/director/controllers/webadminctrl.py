"""
:mod:`webadminctrl`
====================

.. module:: webadminctrl
   :platform: Unix, MacOSX, Windows
   :synopsis: This provides the interface to command line processes.
.. moduleauthor:: Oisin Mulvihill <oisin.mulvihill@gmail.com>

This runs the webadmin without needing to spawnit under another python process.

.. autoclass:: director.controllers.webadminctrl.Controller
   :members:
   :undoc-members:

"""
import os
import logging
import subprocess

import agency
import director
from agency.manager import Manager
from director.controllers import base
from webadmin.scripts import runwebadmin


class Controller(base.Controller):
    """
    This controller typically has the following configuration::

        [agency]
        # Standard options example:
        controller = 'director.controllers.webadminctrl'
        
        # (OPTIONAL) Uncomment to prevent this controller from being used.
        #disabled = 'yes'
        
        # (OPTIONAL) When to start the webadmin. It needs the broker
        # running before it will fully start up.
        order = 4
        
        # (OPTIONAL) the root of the web interface into which all other 
        # parts are plugged. This is the default but it can be easily
        # switched and overridden.
        webadmin = 'webadmin'
        
        # The configuration to use for the webadmin. By default it will 
        # use its own which is packaged with the evasion-webadmin
        #config_file = "/path/to/pylons/paste/compatibile/config.ini"

    """

    def setUp(self, config):
        base.Controller.setUp(self, config)
        self.log = logging.getLogger('director.controllers.webadminctrl')
    
        config_file = self.config.get('config_file', None)
        if config_file:
            self.log.info("setUp: creating webadmin with user given config '%s'." % config_file)
        else:
            self.log.info("setUp: creating webadmin with internal configuration.")
            
        self.webadmin = runwebadmin.Run(config_file)


    def start(self):
        from twisted.internet import reactor
        
        if self.webadmin.directorIntegrationIsStarted():
            self.log.error("start: server started already!")
            
        else:
            def _main(data=0):
                self.log.info("start: creating webadmin with internal configuration.")
                self.webadmin.directorIntegrationStart()
            import thread
            thread.start_new_thread(_main, (0,))


    def isStarted(self):
        rc = self.webadmin.directorIntegrationIsStarted()
        self.log.debug("isStarted: rc:%s." % rc)
        return rc
    

    def stop(self):
        self.log.info("stop: shutting down server.")
        self.webadmin.directorIntegrationStop()
        self.log.info("stop: server stop called ok.")
        

    def isStopped(self):
        return not self.isStarted()


    def tearDown(self):
        pass
