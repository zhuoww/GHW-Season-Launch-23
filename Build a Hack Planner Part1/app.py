from flask import Flask, render_template, request, redirect

app = Flask(__name__)

items = []


@app.route('/')
def checklist():
    return render_template('checklist.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item']
    item.append(item)
    return redirect('/')


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = items[item_id - 1]

    if request.method == 'POST':
        new_item = request.form['item']
        items[item_id - 1] = new_item
        return redirect('/')

    return render_template('edit.html', item=item, item_id=item_id)

# Delete


@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    del items[item_id - 1]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
