# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

window_name = "Downhill Daredevil Extreme 2000" # Nom de la fenêtre

crash_report_mail = "nomail@yopmail.com" # Adresse mail du développeur

crash_report_subject = f"Crash Report - {window_name}" # Sujet du mail

crash_report_body = "{win_name} a rencontré une erreur durant son exécution.\n\nVoici l'erreur rencontrée:\n{crash_rep}\n\nInformation machine:\nsystem: {plat_sys} \n time: {dt_now} \n version: {plat_ver} \n architecture:{plat_arch} \n processor:{plat_proc} \n python_v:{plat_pyth_ver}\n\nMail généré par {win_name}"
