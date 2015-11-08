$(document).ready( function () {
    renderTable("#cv_list");
    $('tr').on('click','input[value="Edit"]', editDesc);
});

function renderTable(target) {
    $(target).DataTable({
        'ajax': { 
            'url': '../get_cvs',
            'dataSrc': processData
        },
        'deferRender': true,
        'columns': [
            {'data': 'fields.name', 'title': 'Name'},
            {'data': 'fields.email', 'title': 'Email'},
            {'data': 'fields.phone', 'title': 'Phone'},
            {'data': 'fields.skills', 'title': 'Skills'},
            {'data': 'fields.experience', 'title': 'Experience'},
            {'data': 'fields.education', 'title': 'Education'},
            {'data': 'fields.languages', 'title': 'Languages'},
            {'data': 'fields.edit', 'title': 'Edit'}
        ]
    });
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){ 
        json[i].DT_RowId = json[i].pk;
        json[i].fields.edit = '<a href="'+json[i].pk+'/edit"><input type="button" value="Edit"></a>';
    }
    return json;
}

function editDesc(){
    $('#descModalTitle').text($(this).parents('tr').children('td')[0].innerText);
    $('#descModal').modal('show');
}
