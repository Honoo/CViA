$(document).ready( function () {
    renderTable("#description_list"); 
});

function renderTable(target) {
    $(target).DataTable({
        'ajax': { 
            'url': '../get_job_descriptions',
            'dataSrc': processData
        },
        'deferRender': true,
        'columns': [
            {'data': 'fields._job_title', 'title': 'Job Title'},
            {'data': 'fields._description', 'title': 'Description'},
            {'data': 'fields._location', 'title': 'Location'},
            {'data': 'fields._skills', 'title': 'Skills'},
            {'data': 'fields._skils_weightage', 'title': 'Skills Weightage'},
            {'data': 'fields._experience', 'title': 'Experience'},
            {'data': 'fields._experience_weightage', 'title': 'Experience Weightage'},
            {'data': 'fields._education', 'title': 'Education'},
            {'data': 'fields._education_weightage', 'title': 'Education Weightage'},
            {'data': 'fields._langauges', 'title': 'Languages'},
            {'data': 'fields._langauges_weightage', 'title': 'Languages Weightage'},
            {'data': 'fields.edit', 'title': 'Edit Description'},
            {'data': 'fields.match_cv', 'title': 'Match CVs'}
        ]
    });
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){ 
        json[i].DT_RowId = json[i].pk;
        json[i].fields.edit = '<input type="button" value="Edit">';
        json[i].fields.match_cv = '<input type="button" value="Match CVs">';
    }
    return json;
}

