var tea = require('tea');

var clear     = 'string to be encrypted';
var password  = 'BH&^!   ljknca>":{L{}uuj~``BF';
var encrypted = tea.encrypt(clear,     password);
var decrypted = tea.decrypt(encrypted, password);

console.log(clear, encrypted, decrypted);
//--> 'string to be encrypted', 'xR4q8OXWSShGk/LYrCQNLWET1GtXooG3', 'string to be encrypted'