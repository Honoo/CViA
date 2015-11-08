$(document).ready( function () {
    renderTable("#cv_list"); 
});

function renderTable(target) {
    $(target).DataTable({
        'ajax': { 
            'url': '../list',
            'dataSrc': processData
        },
        'deferRender': true,
        'columns': [
            {'data': 'fields._anime_name', 'title': 'Anime Title'},
            {'data': 'fields._anime_name_jap', 'title': 'Japanese Title'},
            {'data': 'fields._season_no', 'title': 'Season'},
            {'data': 'fields._episodes_watched', 'title': 'Episodes Watched'},
            {'data': 'fields._total_episodes', 'title': 'Total Episodes'},
            {'data': 'fields.status', 'title': 'Status'}
        ]
    });
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){ 
        var ep = json[i].fields._episodes_watched;
        var tp = json[i].fields._total_episodes;
        var str = '<span class="label label-info">Completed</span>';
        if(ep === 0) str = '<span class="label label-warning">Pending</span>';
        else if(ep < tp) str = '<span class="label label-success">In Progress</span>';   
        json[i].DT_RowId = json[i].pk
        json[i].fields.status = str;
    }
    return json;
}

