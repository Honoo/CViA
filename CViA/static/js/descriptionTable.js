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
            {'data': 'fields.job_title', 'title': 'Job Title'},
            {'data': 'fields.description', 'title': 'Description'},
            {'data': 'fields.location', 'title': 'Location'},
            {'data': 'fields.skills', 'title': 'Skills'},
            {'data': 'fields.skils_weightage', 'title': 'Skills Weightage'},
            {'data': 'fields.experience', 'title': 'Experience'},
            {'data': 'fields.experience_weightage', 'title': 'Experience Weightage'},
            {'data': 'fields.education', 'title': 'Education'},
            {'data': 'fields.education_weightage', 'title': 'Education Weightage'},
            {'data': 'fields.langauges', 'title': 'Languages'},
            {'data': 'fields.langauges_weightage', 'title': 'Languages Weightage'},
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

