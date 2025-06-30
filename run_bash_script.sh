nohup ./run_solver.sh > solver_script_log.txt 2>&1 && 
\ echo -e "Subject: bash script done\n\n$(cat solver_script_log.txt)" | msmtp -a gmail jiayiw@gate
ch.edu &