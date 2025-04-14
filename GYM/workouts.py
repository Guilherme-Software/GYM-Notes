<<<<<<< HEAD
from flask import (
    Blueprint, flash, request, render_template, url_for, redirect
)

from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('workouts', __name__)

#wokout page
@bp.route('/workouts/<int:id>', methods=('GET', 'POST'))
@login_required
def user_workouts(id):
    db = get_db()
    workout = db.execute(
        """SELECT u.id AS user_id, w.*
            FROM user u
            JOIN workout w ON u.id = w.user_id
            WHERE u.id = ?""",
        (id,)
    ).fetchone()

    selected_day = request.form.get('day')

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if request.method == 'POST':
        error = None

        #workout name.
        for day in days:
            value = request.form[f'workout_{day.lower()}']
            if value is "":
                error = f"Name of the Workout {day} is required to continue."
                break
            
            if error:
                flash(error)

        #see if gonna insert or update
            else:
                search = db.execute(
                    "SELECT * from workout WHERE user_id = ?",
                    (id,)
                ).fetchone()

        #insert week workout name.
        if search is None:
            db.execute(
                "INSERT INTO workout (user_id, workout_monday, workout_tuesday, workout_wednesday, workout_thursday, workout_friday, workout_saturday, workout_sunday)"
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                (id),
                request.form.get('workout_monday'),
                request.form.get('workout_tuesday'),
                request.form.get('workout_wednesday'),
                request.form.get('workout_thursday'),
                request.form.get('workout_friday'),
                request.form.get('workout_saturday'),
                request.form.get('workout_sunday')
            )
                )
            db.commit()
        

        #update week workout name.
        else:
            db.execute(
            """
            UPDATE workout
                SET workout_monday = ?, 
                workout_tuesday = ?, 
                workout_wednesday = ?, 
                workout_thursday = ?, 
                workout_friday = ?, 
                workout_saturday = ?, 
                workout_sunday = ?
            WHERE user_id = ?
            """,
            (
                request.form.get('workout_monday'),
                request.form.get('workout_tuesday'),
                request.form.get('workout_wednesday'),
                request.form.get('workout_thursday'),
                request.form.get('workout_friday'),
                request.form.get('workout_saturday'),
                request.form.get('workout_sunday'),
                id
            )
            )
            db.commit()
            

        if error is not None:
            flash(error)

        else:
            return redirect(url_for('notes.user_notes', day=selected_day, id=workout["user_id"]))


    return render_template("workouts.html", days=days, workout=workout)
=======
from flask import (
    Blueprint, flash, request, render_template, url_for, redirect
)

from GYM.auth import login_required
from GYM.db import get_db

bp = Blueprint('workouts', __name__)

#wokout page
@bp.route('/workouts/<int:id>', methods=('GET', 'POST'))
@login_required
def user_workouts(id):
    db = get_db()
    workout = db.execute(
        """SELECT u.id AS user_id, w.*
            FROM user u
            JOIN workout w ON u.id = w.id
            WHERE u.id = ?""",
        (id,)
    ).fetchone()

    selected_day = request.form.get('day')

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if request.method == 'POST':
        error = None

        #workout name.
        for day in days:
            value = request.form[f'workout_{day.lower()}']
            if value is None:
                error = "Name of the Workout is required"
                break
            
            if error:
                flash(error)

        #see if gonna insert or update
        search = db.execute(
            "SELECT * from workout WHERE id = ?",
            (id,)
        ).fetchone()

        #insert week workout name.
        if search is None:
            db.execute(
                "INSERT INTO workout (id, workout_monday, workout_tuesday, workout_wednesday, workout_thursday, workout_friday, workout_saturday, workout_sunday)"
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                (id),
                request.form.get('workout_monday'),
                request.form.get('workout_tuesday'),
                request.form.get('workout_wednesday'),
                request.form.get('workout_thursday'),
                request.form.get('workout_friday'),
                request.form.get('workout_saturday'),
                request.form.get('workout_sunday')
            )
                )
            db.commit()
            return redirect(url_for('notes.user_notes', day=selected_day, id=workout["user_id"]))
        
        #update week workout name.
        else:
            db.execute(
            """
            UPDATE workout
                SET workout_monday = ?, 
                workout_tuesday = ?, 
                workout_wednesday = ?, 
                workout_thursday = ?, 
                workout_friday = ?, 
                workout_saturday = ?, 
                workout_sunday = ?
            WHERE id = ?
            """,
            (
                request.form.get('workout_monday'),
                request.form.get('workout_tuesday'),
                request.form.get('workout_wednesday'),
                request.form.get('workout_thursday'),
                request.form.get('workout_friday'),
                request.form.get('workout_saturday'),
                request.form.get('workout_sunday'),
                id
            )
            )
            db.commit()
            return redirect(url_for('notes.user_notes', day=selected_day, id=workout["user_id"]))

    return render_template("workouts.html", days=days, workout=workout)
>>>>>>> 43d1475e80626c81c539e548dce0b0f7a9df358c
