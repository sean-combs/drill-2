

def gather_info(event=None):
    name = document.getElementById("name_input").value
    age = document.getElementById("age_input").value
    school = document.getElementById("school_input").value

    document.getElementById("output_name").innerText = name
    document.getElementById("output_age").innerText = age
    document.getElementById("output_school").innerText = school

    notes = f"{name} is currently {age} years old and studies at {school}. This information was gathered through input fields and displayed using a multiline string in Python via PyScript."
    document.getElementById("output_notes").innerText = notes

btn = document.getElementById("generate_btn")
btn.addEventListener("click", gather_info)




  