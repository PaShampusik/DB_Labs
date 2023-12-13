using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Model
    {
        public Model()
        {
            Products = new HashSet<Product>();
        }

        public int Id { get; set; }
        public string Name { get; set; } = null!;
        public DateOnly Year { get; set; }
        public int MarkId { get; set; }

        public virtual Mark Mark { get; set; } = null!;
        public virtual ICollection<Product> Products { get; set; }
    }
}
