$('.button').click(function(){
    var direction = $(this).attr('name')
    $.ajax({
        url : '/move_mario',
        dataType : 'json',
        data: {
            'direction': direction
          },

        success : function(response){
            $('#table_game').html(response['game_updated']);
            return false;
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
});