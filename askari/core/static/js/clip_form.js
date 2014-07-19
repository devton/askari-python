$(function(){

    startAce = function() {
        var textarea = $('textarea#id_sql_query');
        console.log(textarea.width());
        console.log(textarea.height());

        var editDiv = $('<div>', {
            position: 'absolute',
            width: textarea.width(),
            height: textarea.height(),
            'class': textarea.attr('class')
        }).insertBefore(textarea);

        textarea.css('visibility', 'hidden');

        var editor = ace.edit(editDiv[0]);
        editor.renderer.setShowGutter(true);

        editor.getSession().setUseWrapMode(true);
        editor.getSession().setValue(textarea.val());
        editor.getSession().setMode("ace/mode/sql");

        textarea.closest('form').submit(function () {
            textarea.val(editor.getSession().getValue());
        });

        $('.ace_editor').css({'padding':'0'});

        editor.setTheme("ace/theme/chrome");
    }

    $('a.sql-query-selector').on('click', function() {
       if($('.ace_editor')) {
           $('.ace_editor').remove();
           setTimeout('startAce()', 100);
       } else {
        startAce();
       }
    });

    if($('a.sql-query-selector').length == 0){
      startAce();
    }

});
