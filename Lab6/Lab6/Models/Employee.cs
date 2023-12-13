using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class Employee
    {
        public int Id { get; set; }
        public int? UserId { get; set; }
        public DateTime HireDate { get; set; }

        public virtual User? User { get; set; }
    }
}
