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
            //{'data': 'fields.skills_weightage', 'title': 'Skills Weightage'},
            {'data': 'fields.experience', 'title': 'Experience'},
            //{'data': 'fields.experience_weightage', 'title': 'Experience Weightage'},
            {'data': 'fields.education', 'title': 'Education'},
            //{'data': 'fields.education_weightage', 'title': 'Education Weightage'},
            {'data': 'fields.languages', 'title': 'Languages'},
            {'data': 'fields.weights_string', 'title': 'Weightage'},
            {'data': 'fields.edit', 'title': 'Edit'},
            {'data': 'fields.match_cv', 'title': 'Match CVs'},
            {'data': 'fields.delete_job', 'title': 'Delete'}
        ]
    });
}

function processData(json){
    var len = json.length;
    for(var i=0; i < len; i++){ 
        json[i].DT_RowId = json[i].pk;
        json[i].fields.edit = '<a href="'+json[i].pk+'/edit"><input type="button" value="Edit"></a>';
        json[i].fields.match_cv = '<a href="../job_match/'+json[i].pk+'"><input type="button" value="Match CVs"></a>';
        json[i].fields.delete_job = '<a href="../delete_job/'+json[i].pk+'"><input type = "button" value="Delete"></a>';
        json[i].fields.weights_string = 
            json[i].fields.skills_weightage + ":" + 
            json[i].fields.experience_weightage + ":" + 
            json[i].fields.education_weightage + ":" + 
            json[i].fields.languages_weightage;
    }
    return json;
}
