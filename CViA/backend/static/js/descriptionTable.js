$(document).ready( function () {
    renderTable("#description_list");
    $('tr').on('click','input[value="Edit"]', editDesc);
    $('tr').on('click','input[value="Match CVs"]', matchCVs);
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
            {'data': 'fields.skills_weightage', 'title': 'Skills Weightage'},
            {'data': 'fields.experience', 'title': 'Experience'},
            {'data': 'fields.experience_weightage', 'title': 'Experience Weightage'},
            {'data': 'fields.education', 'title': 'Education'},
            {'data': 'fields.education_weightage', 'title': 'Education Weightage'},
            {'data': 'fields.languages', 'title': 'Languages'},
            {'data': 'fields.languages_weightage', 'title': 'Languages Weightage'},
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

function editDesc(){
    $('#descModalTitle').text($(this).parents('tr').children('td')[0].innerText);
    $('#descModal').modal('show');
}

function matchCVs(){

}
