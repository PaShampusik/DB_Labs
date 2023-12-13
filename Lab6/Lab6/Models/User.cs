using System;
using System.Collections.Generic;

namespace Lab6.Models
{
    public partial class User
    {
        public User()
        {
            Employees = new HashSet<Employee>();
            Logs = new HashSet<Log>();
            Orders = new HashSet<Order>();
            Reviews = new HashSet<Review>();
        }

        public int Id { get; set; }
        public string Login { get; set; } = null!;
        public string Password { get; set; } = null!;
        public string Phone { get; set; } = null!;
        public string? Email { get; set; }
        public bool IsStaff { get; set; }
        public bool IsSuperuser { get; set; }

        public virtual ICollection<Employee> Employees { get; set; }
        public virtual ICollection<Log> Logs { get; set; }
        public virtual ICollection<Order> Orders { get; set; }
        public virtual ICollection<Review> Reviews { get; set; }
    }
}
