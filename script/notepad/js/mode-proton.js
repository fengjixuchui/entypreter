define('ace/mode/duckycode', function(require, exports, module) {

    var oop = require("ace/lib/oop");
    var TextMode = require("ace/mode/text").Mode;
    var ExampleHighlightRules = require("ace/mode/duckycode_highlight_rules").ExampleHighlightRules;
    
    var Mode = function() {
        this.HighlightRules = ExampleHighlightRules;
    };
    oop.inherits(Mode, TextMode);


    (function() {
        // Extra logic goes here. (see below)
    }).call(Mode.prototype);
    
    exports.Mode = Mode;
    });
    
    define('ace/mode/duckycode_highlight_rules', function(require, exports, module) {
    
    var oop = require("ace/lib/oop");
    var TextHighlightRules = require("ace/mode/text_highlight_rules").TextHighlightRules;
    
    var ExampleHighlightRules = function() {
    
        this.$rules = {
         start: [{
            token: 'entity.name.function',
            regex: '^(VERBOSE|SPOOL|API|SOUNDS)'
         },
         {
            token: 'string',
            regex: '(^PYEXEC|#include <psio>)'
         },
         {
            token: 'string',
            regex: '(^PYEXEC|#include <psio>)'
         },
         {
             token: 'comment',
             regex: '(^#).*$'
         },
         {
             token: 'constant.language',
             regex: '^(JOBS|STAGERS|ZOMBIES|CREDS|DOMAIN|REPEAT)$'
         },
         {
            token: 'support.type',
            regex: '^(USE|SET|LOAD|BACK|DELAY|SRVHOST|SRVPORT)'
         },
         {
            token: 'keyword',
            regex: '^(UNSET|INFO|KILL|RUN)'
         },
         {
            token: 'keywordMapper',
            regex: "[a-zA-Z][a-zA-Z0-9_]*\\b"
         },
           ] 
        }
        
    }
    
    oop.inherits(ExampleHighlightRules, TextHighlightRules);
    
    exports.ExampleHighlightRules = ExampleHighlightRules;
    });
    
    
