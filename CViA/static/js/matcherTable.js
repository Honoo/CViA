$(document).ready( function () {
    renderTable("#cv_list"); 
});

function renderTable(target) {
    $(target).DataTable({
        'ajax': { 
            'url': '../get_cvs',
            'dataSrc': processData,
            'order': [[ 0, "desc" ]] // Order by the first column (score)
        },
        'deferRender': true,
        'columns': [
            {'data': 'fields.score', 'title': 'Total Score'},
            {'data': 'fields.name', 'title': 'Name'},
            {'data': 'fields.education', 'title': 'Education'},
            {'data': 'fields.skills', 'title': 'Skills'},
            {'data': 'fields.experience', 'title': 'Experience'},
            {'data': 'fields.languages', 'title': 'Languages'},
        ]
    });
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){    
        json[i].DT_RowId = json[i].pk;
    }
    return json;
}

