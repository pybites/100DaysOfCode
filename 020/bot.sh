cmd="$HOME/bin/python3/bin/python3.5 domain_mentions.py"
until $cmd; do
    echo "Slack bot crashed with exit code $?.  Respawning.." >> bot.err
    sleep 1
done
