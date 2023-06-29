# Deploy 
pip3 install -r deps.txt

# Run Migration
python3 manage.py migrate

python3 manage.py collectstatic --no-input