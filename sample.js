var webdriver = require('selenium-webdriver');

var driver = new webdriver.Builder().withCapabilities(webdriver.Capabilities.firefox()).build();

driver.get('http://www.github.com');

console.log(html_src);