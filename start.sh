#!/bin/bash

echo "Starting Django Backend..."
source venv/bin/activate
python manage.py runserver 8000 &
BACKEND_PID=$!

echo "Starting Vite Frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!

echo "Both services started."
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"

# Wait for any process to exit
wait $BACKEND_PID $FRONTEND_PID
