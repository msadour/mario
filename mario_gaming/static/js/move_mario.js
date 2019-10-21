$('.button').click(function(){
    var direction = $(this).attr('name')
    $.ajax({
        url : '/move_mario',
        dataType : 'json',
        data: {
            'direction': direction
          },

        success : function(response){
            if (response['win'] == false){
                $('#table_game').html(response['game_updated']);
                $('#table_button').html(response['new_possibilities']);
            } else {
                $('#table_game').html("<p>You win ! </p>");
                $('#table_button').html("");
            }
            return false;
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
});