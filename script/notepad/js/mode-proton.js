define('ace/mode/protoncode', function(require, exports, module) {
    var oop = require("ace/lib/oop");
    var TextMode = require("ace/mode/text").Mode;
    var ExampleHighlightRules = require("ace/mode/protoncode_highlight_rules").ExampleHighlightRules;
    
    var Mode = function() {
        this.HighlightRules = ExampleHighlightRules;
    };
    oop.inherits(Mode, TextMode);


    (function() {
        // Extra logic goes here. (see below)
    }).call(Mode.prototype);
    
    exports.Mode = Mode;
    });
    
    define('ace/mode/protoncode_highlight_rules', function(require, exports, module) {
    
    var oop = require("ace/lib/oop");
    var TextHighlightRules = require("ace/mode/text_highlight_rules").TextHighlightRules;
    
    var ExampleHighlightRules = function() {
    
        this.$rules = {
         start: [
         {
            token: 'Modules',
            regex: '(enum_domain_info)'
         },
         {
            token: 'entity.name.function',
            regex: '(|^)(verbose|spool|api|sounds)( |$)'
         },
         {
            token: 'string',
            regex: '(|^)(pyexec|edit|shell|logo|load)( |$)'
         },
         {
             token: 'comment',
             regex: '(#).*$'
         },
         {
             token: 'constant.language',
             regex: '(|^)(jobs|stagers|zombies|creds|domain|repeat|info|help|modules)( |$)'
         }, 
         {
            token: 'support.function',
            regex: '(|^)(use|set|delay|print|run)( |$)'
         },       	
         {
            token: 'keyword',
            regex: '(|^)(unset|kill|exit|back|clear|nopse)( |$)'
         },
         {
            token: 'support.function',
            regex: "[0-9]"
         },
         ] 
        }
        
    }
    
    oop.inherits(ExampleHighlightRules, TextHighlightRules);
    
    exports.ExampleHighlightRules = ExampleHighlightRules;
    });
    
    
