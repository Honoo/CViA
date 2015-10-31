var path = require('path');
var SomeHR = require('./src/SomeHR')();
require('colors');
var success = false;
// setTimeout(main, 2000);

main()

function main() {
  var files = process.argv.slice(2);
  var exitCode;
  if (files.length === 0) {
    console.log("Usage: node parse.js [file ...]");
  } else {
    handleFile(files);
  }
  process.on('exit', function(code) {
    if (!success) {
      process.exit(code === 0 ? -1 : code);
    }
  })
 }

function handleFile(files, err) {
    var Iam = SomeHR,
      ParseBoy,
      savedFiles = 0;

    if (err) {
      return Iam.explainError(err);
    }
    if (!files.length) {
      return Iam.nothingToDo();
    }

    /** @type {ParseBoy} */
    ParseBoy = Iam.needSomeoneToSortCV();
    ParseBoy.willHelpWithPleasure(files, function (PreparedFile) {
      ParseBoy.workingHardOn(PreparedFile, function (Resume) {
        ParseBoy.storeResume(PreparedFile, Resume, __dirname + '/compiled', function (err) {
          if (err) {
            return ParseBoy.explainError(err);
          }

          savedFiles += 1;

          if (savedFiles == files.length) {
            console.log('Done');
            success = true;
          }
        })
      });
    });
  }