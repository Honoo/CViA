$(document).ready( function () {
    renderTable("#cv_list");
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
            {'data': 'fields.edit', 'title': 'Edit'},
            {'data': 'fields.delete_cv', 'title': 'Delete'}
        ]
    });
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){ 
        json[i].DT_RowId = json[i].pk;
        json[i].fields.edit = '<a href="'+json[i].pk+'/edit"><input type="button" value="Edit"></a>';
        json[i].fields.delete_cv = '<a href="../delete_cv/'+json[i].pk+'"><input type = "button" value="Delete"></a>';
    }
    return json;
}
