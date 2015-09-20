class CreateListings < ActiveRecord::Migration
  def change
    create_table :listings do |t|
      t.string :name
      t.text :descriptions
      t.decimal :price

      t.timestamps
    end
  end
end
