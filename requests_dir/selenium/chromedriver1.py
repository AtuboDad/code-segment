# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# extension for https://sites.google.com/a/chromium.org/chromedriver/
# Experimental, maybe change in the future
# Created by <hzsunshx> 2017-01-20

from __future__ import absolute_import

import atexit
import six
from selenium import webdriver

if six.PY3:
    import subprocess
    from urllib.error import URLError
else:
    from urllib2 import URLError
    import subprocess32 as subprocess


class ChromeDriver(object):
    def __init__(self, d, port=9515):
        self._d = d
        self._port = port

    def _launch_webdriver(self):
        print("start chromedriver instance")
        p = subprocess.Popen(['chromedriver_86.exe', '--port=' + str(self._port)])
        try:
            p.wait(timeout=2.0)
            return False
        except subprocess.TimeoutExpired:
            return True

    def driver(self, device_ip=None, package=None, attach=True, activity=None, process=None):
        """
        Args:
            - package(string): default current running app
            - attach(bool): default true, Attach to an already-running app instead of launching the app with a clear data directory
            - activity(string): Name of the Activity hosting the WebView.
            - process(string): Process name of the Activity hosting the WebView (as given by ps).
                If not given, the process name is assumed to be the same as androidPackage.
        Returns:
            selenium driver
        """
        if device_ip is not None:
            subprocess.call(['adb', 'tcpip', '5555'])
            subprocess.Popen(['adb', 'connect', str(device_ip)])

        app = self._d.current_app()
        package = app['package']
        print('app', app)
        if package == 'com.tencent.mm':
            process = 'com.tencent.mm:tools'
        capabilities = {
            'chromeOptions': {
                'platformName': 'Android',
                'androidDeviceSerial': self._d.serial,
                'androidPackage': package or app['package'],
                'androidUseRunningApp': attach,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
                'androidActivity': activity or app['activity'],
            }
        }

        try:
            # dr = webdriver.Remote('http://localhost:%d' % self._port, capabilities)
            # dr = webdriver.Remote(command_executor='http://127.0.0.1:%d/wd/hub' % self._port,
            #                       desired_capabilities=capabilities)

            options = webdriver.EdgeOptions()
            options.add_experimental_option('androidDeviceSerial', self._d.serial)
            # options.add_experimental_option('androidActivity', '..plugin.webview.ui.tools.WebViewUI')
            options.add_experimental_option('androidPackage', app.get('package'))
            options.add_experimental_option('androidUseRunningApp', True)
            print('package', package)
            if package == 'com.tencent.mm':
                options.add_experimental_option('androidProcess', 'com.tencent.mm:tools')
            # dr = webdriver.Edge('chromedriver_95.exe', options=options)
            # dr = webdriver.Edge('chromedriver_86.exe', options=options, capabilities={})
            dr = webdriver.Edge('msedgedriver.exe')
            dr.implicitly_wait(8)
        except URLError:
            self._launch_webdriver()
            dr = webdriver.Remote('http://localhost:%d' % self._port, capabilities)

        # always quit driver when done
        atexit.register(dr.quit)
        return dr

    def windows_kill(self):
        subprocess.call(['taskkill', '/F', '/IM', 'chromedriver.exe', '/T'])


if __name__ == '__main__':
    import atx

    d = atx.connect()
    driver = ChromeDriver(d).driver()
    elem = driver.find_element_by_link_text(u"登录")
    elem.click()
    driver.quit()
