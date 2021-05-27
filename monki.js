// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/crist/Desktop/Cripto/Tarea3/index.html
// @icon         https://www.google.com/s2/favicons?domain=undefined.
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    var tea = require('tea');

    var clear     = 'hola';
    var password  = 'BH&^!   ljknca>":{L{}uuj~``BF';
    var encrypted = tea.encrypt(clear,     password);
    var decrypted = tea.decrypt(encrypted, password);

    console.log(clear, encrypted, decrypted);

    div[0].innerHTML = 'mensaje cifrado: '+clear;
    console.log(clear.toString(CryptoJS.enc.Utf8))
})();