#!/bin/bash

mongosh <<EOF
use booking;
db.createUser(
  {
    user: 'dev-user',
    pwd: 'dev-pass',
    roles: [{ role: 'readWrite', db: 'booking' }],
  },
);
db.createCollection('users');
EOF
