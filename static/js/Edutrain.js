function ShowHidePanel(p_val) {
   try {

       ShowHideControl("div_1", 0);
       ShowHideControl("div_2", 0);
       ShowHideControl("div_3", 0);
       ShowHideControl("div_4", 0);

       SetActiveControl("li_1", 0);
       SetActiveControl("li_2", 0);
       SetActiveControl("li_3", 0);
       SetActiveControl("li_4", 0);
               
       if (p_val == 1) {
           ShowHideControl("div_1", 1);
           SetActiveControl("li_1", 1);
       }
       if (p_val == 2) {
           ShowHideControl("div_2", 1);
           SetActiveControl("li_2", 1);
       }
       if (p_val == 3) {
           ShowHideControl("div_3", 1);
           SetActiveControl("li_3", 1);
       }
       if (p_val == 4) {
           ShowHideControl("div_4", 1);
           SetActiveControl("li_4", 1);
       }
       if (p_val == 5) {
        ShowHideControl("div_5", 1);
        SetActiveControl("li_5", 1);
    }
   }
   catch (err) {
       alert('ShowHidePanel() - Error in JScript');
   }
}

function ShowHideControl(p_ctrl_name, p_is_show) {
   try {
       p_ctrl_ref = window.document.getElementById(p_ctrl_name);
       if (p_is_show == 1) {
           p_ctrl_ref.style.display = "";
       }
       else {
           p_ctrl_ref.style.display = "none";
       }

   }
   catch (err) {
   }
}

function SetActiveControl(p_ctrl_name, p_is_active) {
   try {
       p_ctrl_ref = window.document.getElementById(p_ctrl_name);
       if (p_is_active == 1) {
           p_ctrl_ref.className = "active";
       }
       else {
           p_ctrl_ref.className = "";
       }

   }
   catch (err) {
   }
}
