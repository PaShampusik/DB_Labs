using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Wheel
    {
        public Wheel()
        {
            Products = new HashSet<Product>();
        }

        public int Id { get; set; }
        public string Type { get; set; } = null!;
        public int? Size { get; set; }

        public virtual ICollection<Product> Products { get; set; }
    }
}
